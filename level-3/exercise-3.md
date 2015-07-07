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
    But what is `jsonify`?
    
    > ![Question](../images/question.png) You know the answer!  We've done it
    before, what is at least one way you can find out what something does in 
    Python/PyCharm?
    
#### Step 2: Enable API Support for Retrieving Information on a Specific Friend
```python
...
@app.route('/api/v1/friends', methods=['GET'])
    def get_friends():
        """Return a representation of the collection of friend resources."""
        return jsonify({"friends": friends})
...
```
        