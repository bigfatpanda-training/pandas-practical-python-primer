[Previous](exercise-2.md) |  [Next](exercise-4.md)
## Add HTTP GET Support to our Web Service API
The first thing that we are going to do is add support for HTTP GET operations
to our API.  We will add this for both the **resource collection** and 
**individual resource** levels.

> ![Question](../images/question.png) What is the difference between those two terms?

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
    
    
#### Step 2: Test your API
In order to test your API, you'll need two terminal windows open with active
SSH sessions in your Vagrant VM.  
* For Mac users, this should be relatively easy.  You can open multiple tabs 
in the default `terminal` application, or use the excellent iTerm2 for even
better options.

* Windows users, time for a little bit more pain.  You'll need to have two 
separate instances of Git Bash running and just position the windows next to 
each other.  It might not be very clear on how to start multiple instances of 
the same application in any given version of windows, so this might take a bit
to get setup.

Once you have two SSH terminal sessions open do the following:
* In the first terminal session go to `/vagrant/trainee-area/level-3-creating-web-services/trainee-friends-api`
and execute `python run_server.py`.  This will start the test HTTP server
and load your Flask app into it.  The output will look like this if everything
worked correctly:

    ```
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    ```
* In your second terminal window, you can issue `curl` commands to access
various methods of your API.  Test your first method with the following command:
`curl 127.0.0.1:5000/api/v1/friends`.  
* You should get the following response:
    
    ```
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
        }
      ]
    }
    ```
    
    > > ![Reminder](../images/reminder.png) Both terminal sessions need to have
    active SSH connections to the Vagrant VM (`vagrant ssh`) for this to work correctly.
    
#### Step 3: Enable API Support for Retrieving Information on a Specific Friend
```python
...
@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id):
    """Return a representation of a specific friend or an error."""
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
modify the HTTP status code that would be returned by using `jsonify` alone (200).

    > ![Question](../images/question.png) What are we changing the HTTP status code
    > to?  Why is that important?

##### Testing
* Drop to the command-line and try to access your new method: 
`curl 127.0.0.1:5000/api/v1/friends/VinDi`.  
    * Did you get this? `NameError: name 'make_response' is not defined`
    * This is because we're referencing an name that is not currently defined. 
    It still needs to be imported from the `flask` package.
    * Update your `from flask import ...` statement to include `make_response`.
    
* Once you've fixed the code, notice that the Flask test HTTP server restarts
automatically?  This is a handy feature for development, but would not be
present in production environments.

* Try the curl command again and you should get the following output:
    ```
    {
      "email": "vdiesel4@supercool.edu",
      "first_name": "Vin",
      "id": "VinDi",
      "last_name": "Diesel",
      "notes": "Really annoying guy.  Will never amount to anything.",
      "telephone": "I-HIT-PEOPLE"
    }
    ```

> ![Alert](../images/alert.png) We've introduced a bug here that might not be
> be immediately obvious.  What happens when we query for `BFP`?  What about
> `bfp`?  How might we account for this?

