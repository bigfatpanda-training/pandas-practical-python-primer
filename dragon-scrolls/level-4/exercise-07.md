[Previous](exercise-06.md) |  [Next](exercise-08.md)
## Exercise 7: Debugging HTTP POST Support
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_06)

Let's improve your POST support by killing the bugs that we discovered at the
end of the previous section.

### There Is No Secret Ingredient: Create a Temporary Test Harness
When an error is encountered inside a Flask application, the program will
often try to handle the error on your behalf so that the API doesn't come
crashing down.  This is a good thing, otherwise your entire program would
terminate and no new requests would be responded to.

An example of this is when we passed JSON with syntax errors into the API, it
returned a 400 (which is correct status code to return in such a case).  
The downside to this is that sometimes it can swallow error information 
that we need to debug our program.
 
To account for this, we need to create a sort of temporary testing harness that 
will allow us to capture the exception information and return it to the client
for debugging purposes.

- Update the `create_friend` function to look like this:

    ```python
    @app.route('/api/v1/friends', methods=['POST'])
    def create_friend() -> Response:
        """
        Create a new friend resource.
    
        Utilize a JSON representation/payload in the request object to
        create a new friend resource.
    
        Returns:
            A flask.Response object.
        """
        import sys
        try:    
            request_payload = request.get_json()
            datastore.create_friend(request_payload)
        except Exception as error:
            response = make_response(
                jsonify(
                    {"errorType": str(sys.exc_info()[0]),
                     "errorMessage": str(sys.exc_info()[1]),
                     "errorLocation": sys.exc_info()[2].tb_lineno}),
                    400)
            return response
        else:
            response = make_response(
                jsonify({"message": "Friend resource created."}), 201)
            return response
    ```
    
    - In the exception handler, we are catching all children of the Exception
    class, which basically means that we'll be catching all exceptions.  
    - This is a big no-no for production code, but will be useful to us as 
    we are developing because it will allow us to catch all errors and report
    on them.
    - Now when we make a call to our API, it will catch the exceptions and 
    return information on them in the HTTP response for us to analyze.
    - Notice that we are importing the `sys` module inside of our function here.
    This is a violation of PEP8 and shouldn't persist when we're done 
    debugging our code.
        - So why did I put it here?  Because we only need it inside this 
        function and having it in an odd location will help me remember that
        it needs to be removed.
        - The `sys.exc_info` function allows us to extract extra information
        about the exception currently being handled that will be helpful to 
        us in debugging.  You can always check out its 
        [documentation]((https://docs.python.org/3/library/sys.html#sys.exc_info) 
        for more info.
    
    > ![info](../images/information.png) You've seen the `try/except` syntax 
    > before, but if you need a refresher on how it works, consult the 
    > [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) 
    
### Squash the Invalid JSON Syntax Bug
If a client sends a request to your API to create a new friend with invalid or
broken JSON syntax they'll get something like this back:

```bash 
>>> 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck" "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>The browser (or proxy) sent a request that this server could not understand.</p>
```

- This is a HTML snippet.  IF given to a browser, it would generate an web
page with an error message for the user.  This is Flask's default behavior
when an attempt to extract JSON from an incoming HTTP request - `request.get_json()` - 
finds invalid JSON and an internal exception/error is thrown.

- We however, are communicating program to program with no browser involved,
so we need to catch the exception before Flask turns it into this HTML message
and do something else with it.

With our test harness in place, we can dig into what what is happening
inside our program **before** Flask handles the error so that we can return 
an appropriate response for an API instead of a HTML fragment.

- Execute the following `curl` command will bad JSON syntax and see what the
test harness gives you back:
 
    ```bash
    >>> 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck" "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
    {
      "errorLocation": 53,
      "errorMessage": "400: Bad Request",
      "errorType": "<class 'werkzeug.exceptions.BadRequest'>"
    }
    ```

- From this, I can tell that the exception occurred at line 53 in my code and
that the error type was a custom error in the `werkzeug` package.  In other 
words, its not a error that is part of the standard library.
    - Your "errorLocation" might not be 53 as your line numbers may 
     not be the exact same as mine.  What's important is that the value
     presented to points to the line of code where the error originated.

    > ![info](../images/information.png) Just like our program requires `Flask`, it 
    > requires the `werkzeug` package.  So when we installed `Flask` from our
    > `requirements.txt` file, it also got installed.
    
- Looking at line 53 (or wherever "errorLocation" points to), we see the 
code responsible for our bug: `request_payload = request.get_json()`.  
    
- We can deduce from this that if there is a call to `request.get_json` 
and the JSON payload has a syntax error, then a `werkzeug.exceptions.BadRequest` 
exception is raised.

- To address this, we need to create an additional `except BadRequest` 
block **before** our `except Exception` block. This will only catch the 
`BadRequest` error and return a message to the user saying that the JSON 
payload had syntax errors:  

    ```python
    # Add the necessary import at the top of the module
    from werkzeug.exceptions import BadRequest
    ...
    
    # Add the try/except block inside create_friend()
    try:
        request_payload = request.get_json()
    except BadRequest as error:
        response = make_response(
            jsonify(
                {"error": "JSON payload contains syntax errors. "
                          "Please fix and try again."}),
                400)
        return response
    except Exception as error:
    ...
    ```

- Try the `curl` call with bad JSON syntax again and you should get this:
    ```
    {
      "error": "JSON payload contains syntax errors. Please fix and try again."
    }
    ```


### Smash the No `content-type:application/json` Header Bug
- Incoming HTTP requests that don't provide a `content-type` header specifying 
the payload as `application/json` appear to succeed in our API:
  
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends -X POST -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
    {
      "message": "Friend resource created."
    }
    ```
    
- However, if you then request your list of friends, you'll see that
something is amiss:

    ```bash
    >>> curl http://127.0.0.1:5000/api/v1/friends
    {
      "friends": [
        {
          "email": "mike@eikonomega.com",
          "firstName": "Big Fat",
          "id": "BFP",
          "lastName": "Panda",
          "notes": "My bestest friend in all the world.",
          "telephone": "574-213-0726"
        },
        {
          "email": "vdiesel4@supercool.edu",
          "firstName": "Vin",
          "id": "VinDi",
          "lastName": "Diesel",
          "notes": "Really annoying guy.  Will never amount to anything.",
          "telephone": "I-HIT-PEOPLE"
        },
        null
      ]
    }
    ```
    
    - You can see that `null` has been added to your list of friends.  **Now,
    I know that some friends can be dull, but there probably are completely 
    `null`.**
    
- Notice that this error is also not caught in our test harness.  This is
because no exception has occurred in our program.  When we call the  
`request.get_json()` method.  It depends on there being a `content-type`
header set to `application/json`.  If it doesn't find one, it assumes
that there is no JSON payload and returns `None`.

- So, you have choice to make now. You can check to see if the return 
value of `request.get_json` is `None` and prevent the call to 
`datastore.create_friend` or you can have a check for that inside of 
`datastore.create_friend`.  

- Since, generally speaking, I think it is better for functions to verify
the validity of arguments they receive, we'll put the check inside of 
`datastore.create_friend`:

    ```python
    def create_friend(data: dict):
        """
        Create a new friend entry is our datastore of friends.
    
        Args:
            data: A dictionary of data for our new friend.
        
        Raises:
            ValueError: If `data` is None.
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new friend resource.")
        friends.append(data)
    ```
    
    - Notice here that we are doing something new here: using the `raise`
    keyword.
    - This allows you to raise exceptions(errors) from your functions/methods. 
    In this case, we use the built-in exception type `ValueError` which
    is a commonly used exception for when a variable's value is not compatible
    with its intended use.
    
- Try to create another friend with invalid JSON syntax.  This is what you
should get now:

    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends -X POST -d '{"id":"dDuk", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
    {
      "errorLocation": 54,
      "errorMessage": "`None` was received when a dict was expected during the attempt to create a new friend resource.",
      "errorType": "<class 'ValueError'>"
    }
    ```
    
- **This is progress.** No new `null` friends are being created.  That said,
our `ValueError` is being caught by our test harness, which means that are
work is still not complete.  It needs to be handled directly - just like
we did with the `BadRequest` exception:

    ```python
    ...
    try:
        request_payload = request.get_json()
        datastore.create_friend(request_payload)
    except BadRequest as error:
        response = make_response(
            jsonify(
                {"error": "JSON payload contains syntax errors. "
                          "Please fix and try again."}),
                400)
        return response
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}), 400)
        return response
    except Exception as error:
    ...
    ```
    
- Verify that this bug is squashed by reusing the curl command above.  You
should get the following response:
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends -X POST -d '{"id":"dDuck", "irstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
    {
      "error": "No JSON payload present.  Make sure that appropriate 
      `content-type` header is included in your request."
    }
    ```
    
### Obliterate the Missing Required Data Element Bug
- Currently our API allows the creation of friend resources with missing 
data elements.  For example, this is what we get when we only specify a
`firstName` in the HTTP request: 
 
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"firstName": "Donald"}'
    {
      "message": "Friend resource created."
    }
    ```
    
- This results in missing data: 
 
    ```bash
    >>> curl http://127.0.0.1:5000/api/v1/friends
        {
      "friends": [
        {
          "email": "mike@eikonomega.com",
          "first_name": "Big Fat",
          "id": "BFP",
          "last_name": "Panda",
          "notes": "My bestest friend in all the world.",
          "telephone": "574-213-0726"
        },
        {
          "email": "vdiesel4@supercool.edu",
          "first_name": "Vin",
          "id": "VinDi",
          "last_name": "Diesel",
          "notes": "Really annoying guy.  Will never amount to anything.",
          "telephone": "I-HIT-PEOPLE"
        },
        {
          "firstName": "Donald"
        }
      ]
    }
    ```
        
- To address this, we need to add a check in `datastore.create_friend`
that verifies if all the required elements are present in an incoming
request:

    ```python
    def create_friend(data: dict):
        ...
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new friend resource.")
    
        required_elements = set(friends[0].keys())
        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))
    
        friends.append(data)
    ```
    
    - The `set(friends[0]keys()` statement creates a `set` object from the 
    key names of the first friend record in the `friends` list.  *Say that
    three times fast!*
    
        > ![info](../images/information.png) A `set` is like a `list` in that
        is can hold an arbitrary number of heterogenous objects.  However,
        unlike a list, it doesn't keep track of insertion order and only allows
        a single entry for a given value.  It also supports very fast 
        comparisons to other sets (which is what we are taking advantage of here).
        
    - The `if` statement requires some explanation. 
        1. `required_elements`, by virtue of being a `set` object has the 
        `issubset` method which allows us to determine if all the elements of 
        the set are included in another container-type.
        
        1. In this case, the container-type object that we want to compare
        is `data`.  That list contains all the key values from the JSON payload
        of the HTTP request that our API received.
        
        1. So the fragment `required_elements.issubset(data)`
        will evaluate to `True` if all the members of `required_elements`
        are present in `data`. Otherwise, it will 
        evaluate to `False`.
        
        1. The `if not` syntax means "if the thing that I'm evaluating does 
        not evaluate to `True` then do X"
             
        1. You can see that we raise a ValueError exception if all the 
        required elements are not present along with a message about 
        what is required.
        
    - With this in place, try the request again and this is what you should
    get:
    
        ```bash
        {
          "error": "Some of the data required to create a friend was not present.  
          The following elements must be present to create a friend: 
          {'notes', 'first_name', 'telephone', 'email', 'last_name', 'id'}"
        }
        ```

### Fix the Bug that Allows You To Create Friends with Identical IDs
- The final bug that we'll be address in this exercise is the proclivity of
our API to allow the creation of duplicate resources.  
    
    - We might have friends that share certain data points, like first/last
    name, or even telephone numbers, but they should still have a unique id
    value.

- You can see this bug in action to executing the following curl commands:
    - Do this one 2x or more times:  `curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`
    
    - Do this to see all your friends:  `curl 127.0.0.1:5000/api/v1/friends`
    
- To fix this issue, let's add one final check to `datastore.create_friend`:
 
    ```python
    ...     
    if not required_elements.issubset(data):
        raise ValueError("Some of the data required to create a friend "
                         "was not present.  The following elements "
                         "must be present to create a friend: {}".format(
            required_elements))

    # Add This
    for friend in friends:
        if data['id'].lower() == friend['id'].lower():
            raise ValueError("A friend already exists with the "
                             "`id` specified: {}".format(data['id']))

    friends.append(data)
    ```
    
- Now verify that you get the correct response when trying to create a 
duplicate friend using the `curl` commands above.  You should get this:

    ```
    {
      "error": "An friend resource already exists with the given id: dDuck1"
    }
    ```
    
> ![Bad Code Alert](../images/alert.png) Keen eyes may have noticed that
our API ultimately returns a `400` status code for this last error condition.
Some would argue that a `409` would be a more appropriate status code.  To
implement that however, we'd have to change other bits of the code.  Feel
free to try if you want to.
        
### Take a Depth Breath and Congratulate Yourself!
You've successfully squished alot of bugs in this section.  Depending on your
personality, this could have been really fun or really, really, awful.

If it was the latter of those two options for you, take heart.  You've made
your API much more bulletproof than it was before. And while that takes time 
and effort, it is absolutely necessary if you want to create web APIs that 
people will actually use in the real world.

To finish off this section, let's remove the test harness that we added to 
`friends.create_friend`at the beginning of this exercise.  After that, make sure  
your function looks like this:

    ```python
    @app.route('/api/v1/friends', methods=['POST'])
    def create_friend() -> Response:
        """
        Create a new friend resource.
    
        Utilize a JSON representation/payload in the request object to
        create a new friend resource.
    
        Returns:
            A flask.Response object.
        """
        try:
            request_payload = request.get_json()
            datastore.create_friend(request_payload)
        except BadRequest as error:
            response = make_response(
                jsonify(
                    {"error": "JSON payload contains syntax errors. "
                              "Please fix and try again."}),
                    400)
            return response
        except ValueError as error:
            response = make_response(
                jsonify({"error": str(error)}), 400)
            return response
        else:
            response = make_response(
                jsonify({"message": "Friend resource created."}), 201)
            return response
    ```
    
> ![Extra Credit](../images/reminder.png) Want another bug to squish? The API
currently allows you to specify additional non-standard data points.  How
might you modify `datastore.create_friend` to prevent this?
    
| [Next Exercise](exercise-08.md)
    