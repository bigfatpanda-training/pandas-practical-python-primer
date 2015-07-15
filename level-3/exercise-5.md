[Previous](exercise-4.md) |  [Next](exercise-6.md)
## Debugging HTTP POST Support in our Web Service API
Let's improve our POST support by killing the bugs that we discovered at the
end of the previous section.

#### Step 1: Create a Generic Try/Except Clause to Capture Exceptions
When an error is encountered inside a Flask application, the program will
often try to handle the error on your behalf so that the API doesn't come
crashing down.  This is a good thing.

An example of this is when we passed JSON with syntax errors into the API, it
returned a 400 (which is correct).  The downside to this is that sometimes it
can swallow error information that we need to debug our program.
 
To account for this, we need to create a sort of temporary testing harness that 
will allow us to capture the exception information and return it to the client
for debugging purposes.

* Update the `create_friend` function to look like this:
    ```python
    @app.route('/api/v1/friends', methods=['POST'])
def create_friend():
    """
    Create a new friend resource.

    Utilize a JSON representation in the request object to create
    a new friend resource.
    """

    try:
        import sys
        request_payload = request.get_json()

        datastore.friends.append(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})

        response = make_response(jsonify({"message": "Friend resource created."}),
                                 201)
    except Exception as error:
        response = make_response(
            jsonify({"errorType": str(sys.exc_info()[0]),
                     "errorMessage": str(sys.exc_info()[1]),
                     "errorLocation": sys.exc_info()[2].tb_lineno}),
            400)

    return response
    ```
    
    * In the exception handler, we are catching all children of the Exception
    class, which basically means that we'll be catching all exceptions.  
    * This is a big no-no for production code, but will be useful to us as 
    we are developing because it will allow us to catch all errors and report
    on them.
    * Now when we make a call to our API, it will catch the exceptions and 
    return information on them in the HTTP response for us to analyze.
    
    > ![alert](../images/alert.png) Notice that we're importing the `sys`
    > module inside the function.  While this is legal, it's not normal or 
    > recommended.  I'm only doing it here because I know this is going to go
    > away after we finish debugging.
    
    > ![info](../images/information.png) You've seen the `try/except` syntax before,
    > but if you need a refresher on how it works, consult the 
    [Python Documentation](https://docs.python.org/2/tutorial/errors.html#handling-exceptions) 
    
#### Step 2: Fix the no `content-type:application/json` Header Bug
* Incoming HTTP requests that don't provide a `content-type` header specifying
the payload as `application/json` result in a `TypeError` exception.  
    * Example: `curl 127.0.0.1:5000/api/v1/friends -X POST -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`
        
        ```
        # HTTP Response
        {
          "errorLocation": 55,
          "errorMessage": "'NoneType' object is not subscriptable",
          "errorType": "<class 'TypeError'>"
        }
        ```
* The keys to pick up from this error message is that the error occured at line 
55 (your location may be slightly different depending on your program line numbers) 
and that an attempt was made to access a key value in a `NoneType` object - 
which is impossible.

* Looking at the code at line 55, I see this statement:
    ```python
    datastore.friends.append(
        {"id": request_payload['id'],
         "first_name": request_payload['firstName'],
         "last_name": request_payload['lastName'],
         "telephone": request_payload['telephone'],
         "email": request_payload['email'],
         "notes": request_payload['notes']})
    ``` 
    * There is only one object here on which I'm trying to access key values:
    `request_payload`.  So that is the object from which the error is being
    generated.  
    * So now the question is why the value bound to that name `None`?  Well, 
    we is that name bound?  
        * It's bound earlier in our method by the following 
        statment: `request_payload = request.get_json()`
    * What can we decipher from this?  When the `content-type` header is present,
    the `request.get_json` method returns a `dict` containing the JSON payload.
    However, when it is not present, the method returns `None` which is causing
    this bug.
    
* The solution is to add a check into our code to verify that `request_payload`
is not `None`.  If it is, the user should be information that the API requires
JSON payloads.
    ```python
    ...
    request_payload = request.get_json()
        
    if request_payload is None:
        error_response = make_response(
            jsonify({"error": "No JSON payload present.  Make sure that "
                              "appropriate `content-type` header is "
                              "included in your request."}),
            400)
        return error_response
    ...
    ```
    
* Verify that this bug is squashed by reusing the curl command above.  You
should get the following response.

    ```
    {
      "error": "No JSON payload present.  Make sure that appropriate 
      `content-type` header is included in your request."
    }
    ```
    
#### Step 3: Fix the Invalid JSON Syntax Bug
This one is a little trickier because the first time we saw the error, it had
been handled internally by Flask so we didn't really know the exception that
was being raised.  

Now with our test harness in place, we can dig into what what is happening
inside our program **before** Flask handles the error so that we can handle 
it ourselves and give better feedback to the client.

* Execute the following `curl` command will bad JSON syntax and see what the
test harness gives you back: 
`curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck" "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`

    ```
    {
      "errorLocation": 43,
      "errorMessage": "400: Bad Request",
      "errorType": "<class 'werkzeug.exceptions.BadRequest'>"
    }
    ```

* From this, I can tell that the exception occured at line 43 in my code and
that the error type was a custom error in the `werkzeug` package.  In other 
words, its not a error that is part of the standard library.

    > ![info](../images/information.png) Just like our program requires `Flask`, it 
    > requires the `werkzeug` package.  So when we installed `Flask` from our
    > `requirements.txt` file, it also got installed.
    
* Looking at line 43, we see the same code that was the source of our last
bug: `request_payload = request.get_json()`.  There is a difference however.
    * In our previous bug, the method returned a `None` value, but still 
    completed without an error.  In this case,
    the method is not completing as expected, it is raising an exception.
    * Because of this the solutions are also different.
    
* So, if there is a call to `request.get_json` and the JSON payload has a syntax
error, then a `werkzeug.exceptions.BadRequest` exception is raised.

* To address this, we need to create an additional `try/except` block around
the call to `request.get_json` that only catches the `werkzeug` error and 
return a message to the user saying that the JSON payload had syntax errors.  

    ```python
    # Add the necessary import at the top of the module
    from flask import Flask, jsonify, make_response, request
    from werkzeug.exceptions import BadRequest
    
    # Add the try/except block inside create_friend()
    try:
        request_payload = request.get_json()
    except BadRequest:
        error_response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. Please "
                              "fix and try again."}),
            400)
        return error_response
        
    
    ```

* Try the `curl` call with bad JSON syntax again and you should get this:
    ```
    {
      "error": "JSON payload contains syntax errors. Please fix and try again."
    }
    ```
    
#### Step 4: Fix the Missing Required Data Element Bug
* Incoming HTTP requests that don't provide all the necessary data points in
the JSON payload result in a `KeyError` exception.  
    * Example: `curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`
        
        ```
        # HTTP Response
        {
          "errorLocation": 71,
          "errorMessage": "'id'",
          "errorType": "<class 'KeyError'>"
        }
        ```
        
    * Let's look at the code that I have at line 71 that is generating a 
    `KeyError` on an attempt to access a dictionary element named `id`:
    
        ```python
        datastore.friends.append(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})
        ```
    
        * This was the same bit of code that caused us problems before when 
        there the incoming HTTP request didn't have a `content-type` header.
        
        * However, the errors are not the same.  The first time, the exception
        was caused by trying to access `None` as if it were a dictionary which 
        resulted in a `TypeError`.  This time, we have a `KeyError` which is 
        raised when you attempt to access a key that doesn't exist on a dictionary.
        
    * What this means is `request_payload` has the JSON content from the 
    request, but that the `id` element isn't in it.  This makes sense 
    because if you check the `curl` command you'll see that this element 
    is indeed missing.
    
    * To address this bug we'll need to create a `set` that holds the names of
    the required elements and an `if` statement
    that verifies that all required data elements are present in the request's
    JSON payload:
    
        ```python
        ...
        required_data_elements = {
            "id", "firstName", "lastName", "telephone", "email", "notes"}
        
        if not required_data_elements.issubset(request_payload.keys()):
            error_response = make_response(
                jsonify(
                    {"error": "Missing required payload elements. "
                              "The following elements are "
                              "required: {}".format(required_data_elements)}),
                404)
            return error_response

        datastore.friends.append(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})
        ...
        ```
        
        > ![info](../images/information.png) A `set` is like a `list` in that
        is can hold an arbitrary number of heterogenous objects.  However,
        unlike a list, it doesn't keep track of insertion order and only allows
        a single entry for a given value.  It also supports very fast 
        comparisons to other sets (which is what we are taking advantage of here).
        
        * The `if` statement requires some explanation. 
            1. `required_data_elements`, 
            by virtue of being a `set` object has the `issubset` method which allows
            us to determine if all the elements of the set are included in another
            container-type object that be converter to a set.
            1. In this case, the container-type object that we want to compare
            to is the list returned from `request_payload.keys()`.  That
            list contains all the key values from the JSON payload.
            1. So the fragment `required_data_elements.issubset(request_payload.keys())`
            will evaluate to `True` if all the members of `required_data_elements`
            are present in `request_payload.keys()`. Otherwise, it will 
            evaluate to `False`.
            1. The `if not` syntax means "if the thing that I'm evaluating does 
            not evaluate to `True` then do X"
             
        * Inside the `if` statement, you can see that a helpful message will
        be returned to the user instead of what we got before.  Try it yourself
        and verify that you get the following response.
        
            ```
            {
              "error": "Missing required payload elements. The following 
              elements are required: {'firstName', 'email', 'notes', 'id', 
              'telephone', 'lastName'}"
            }
            ```

#### Step 5: Fix the Bug that Allows You To Create Friends with Identical IDs
    * As we've seen, the way that the API is currently constructed allows us
    to create multiple friend resources that are identical.  That isn't right.
    Each of our friends should only be in our list once.
        * We might have friends that share certain data points, like first/last
        name, or even telephone numbers, but they should still have a unique id
        value.
    
    * You can see this bug in action to executing the following curl commands:
        * Do this one 2x or more times: `curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`
        * Do this to see all your friends: `curl 127.0.0.1:5000/api/v1/friends`
        
    * Let's add a check into our function that will prevent attempts to 
    add a friend resource with an `id` value that already exists:
     
        ```python
        ...     
        for friend in datastore.friends:
            if request_payload['id'].lower() == friend['id'].lower():
                error_response = make_response(
                    jsonify(
                        {"error": "An friend resource already exists with the "
                                  "given id: {}".format(request_payload['id'])}),
                    400)
                return error_response

        datastore.friends.append(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
        ...
        ```
        
    * Now verify that you get the correct response when trying to create a 
    duplicate friend using the `curl` commands above.  You should get this:
    
        ```
        {
          "error": "An friend resource already exists with the given id: dDuck1"
        }
        ```
        
#### Step 6: Take a Depth Breath and Congratulate Yourself!
You've successfully squished alot of bugs in this section.  Depending on your
personality, this could have been really fun or really, really, awful.

If it was the latter of those two options for you, take heart.  You've made
your API much more bulletproof than it was before. And while that takes time 
and effort, it is absolutely necessary if you want to create web APIs that 
people will actually use in the real world.

To finish off this section, let's remove the test harness that we added at
the beginning of [exercise 4](exercise-4.md).  After that, make sure that 
your `create_friend` function looks like this:

    ```python
    @app.route('/api/v1/friends', methods=['POST'])
    def create_friend():
        """
        Create a new friend resource.
    
        Utilize a JSON representation in the request object to create
        a new friend resource.
        """
    
        try:
            import sys
            try:
                request_payload = request.get_json()
            except BadRequest:
                error_response = make_response(
                    jsonify({"error": "JSON payload contains syntax errors. Please "
                                      "fix and try again."}),
                    400)
                return error_response
    
            if request_payload is None:
                error_response = make_response(
                    jsonify({"error": "No JSON payload present.  Make sure that "
                                      "appropriate `content-type` header is "
                                      "included in your request."}),
                    400)
                return error_response
    
            required_data_elements = {
                "id", "firstName", "lastName", "telephone", "email", "notes"}
    
            if not required_data_elements.issubset(request_payload.keys()):
                error_response = make_response(
                    jsonify(
                        {"error": "Missing required payload elements. "
                                  "The following elements are "
                                  "required: {}".format(required_data_elements)}),
                    404)
                return error_response
    
            datastore.friends.append(
                {"id": request_payload['id'],
                 "first_name": request_payload['firstName'],
                 "last_name": request_payload['lastName'],
                 "telephone": request_payload['telephone'],
                 "email": request_payload['email'],
                 "notes": request_payload['notes']})
    
            response = make_response(jsonify({"message": "Friend resource created."}),
                                     201)
        except Exception as error:
            response = make_response(
                jsonify({"errorType": str(sys.exc_info()[0]),
                         "errorMessage": str(sys.exc_info()[1]),
                         "errorLocation": sys.exc_info()[2].tb_lineno}),
                400)
    
        return response
    ```
    