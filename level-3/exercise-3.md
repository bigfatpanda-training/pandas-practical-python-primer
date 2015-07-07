[Previous](exercise-2.md) |  [Next](exercise-4.md)
## Add HTTP GET Support to our Web Service API
The first thing that we are going to do is add support for HTTP GET operations
to our API.  We will add this for both the **resource collection** and 
**individual resource** levels.

> ![Question](../images/reminder.png) What is the difference between those two terms?

#### Step 1: Enable API Support for Retrieving Information on all our Friends
* Add the following code to `api.py`:
    ```python
    ...
    app = Flask(__name__)
    
    
    @app.route('/api/v1/friends', methods=['GET'])
    def get_friends():
        """Return a representation of the collection of friend resources."""
        return jsonify({"friends": friends})
    ```
* There is a lot going on here. So let's take it line by line.
    * The `@app.route()` is a **decorator**.  Decorators are used in Python 
    programs to dynamically add addition statements that are executed before
    and/or after a given function whenever the name of the function is invoked.
        * They are pretty advanced so we won't really get into the guts of how they
        work here (unless you ask me and then we can Geek out!).
        * What you **do** need to understand is that Flask uses them to tie
        your functions to incoming HTTP requests for a given URL and HTTP method.
        * In this case, it is connecting incoming requests to 
        `www.yourserver.com/api/v1/friends` using the `GET` to this function.
        * So this function will be executed whenever such a request is received.
    
    * You're familiar with the function definition statement and the docstring 
    by now and you also know what the `return` statement does generally speaking.
    But we don't yet know what `jsonify` does? How can you find out?
    
    > ![Question](../images/question.png) You know the answer!  We've done it
    before, what is at least one way you can find out what something does in 
    Python/PyCharm?
    
#### Step 2: Enable API Support for Retrieving Information on a Specific Friend
```python
...
@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id):
    for friend in friends:
        if friend["id"] == id:
            return jsonify(friend)

    error_response = make_response(
        jsonify({"error": "No such friend exists."}), 404)
    return error_response
...
```

Adding the above function/route to `api.py` will enable a client to pull
back information from your API on a specific friend based on the `id` field
of a friend record.
* Notice that in the `@app.route` decorator these is a `<id>` added to the 
end of the URL.  Whenever a URL is requested from Flask that matches the 
pattern, the portion of the URL that would be where `<id>` is will be extracted
from the URL and bound to the name `id` within your program.
    * For example, a request to `www.yourserver.com/api/v1/friends/BFP` would
    result in `BFP` being bound to the name `id`.

* It is because of this that the decorated function `get_friend` accepts
a parameter called `id`.  
* The use of `make_response` is also new in this function. It allows use to 
modify the HTTP status code that would be returned by using `jsonify` alone.

> ![Question](../images/question.png) What are we changing the HTTP status code
> to?  Why is that important?

> ![Alert](../images/alert.png) We've introduced a bug here that might not be
> be immediately obvious.  What happens when we query for `BFP`?  What about
> `bfp`?  How might we account for this?