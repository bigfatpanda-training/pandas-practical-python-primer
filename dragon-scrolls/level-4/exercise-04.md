[Previous](exercise-03.md) |  [Next](exercise-05.md)
## Exercise 4: Adding HTTP GET Support to your API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_03)

The first thing that we are going to do is add support for HTTP GET operations
to our API.  In this exercise, we will add it for the **resource collection** 
and in the next exercise will add it for **individual resources**.

> ![Question](../images/question.png) Do you remember what the difference 
> is between those two terms and how their URLs might differ?

### There Is No Secret Ingredient: [GET] All The Friends
- Add the following code to `friends.py`:
    
    ```python
    @app.route('/api/v1/friends', methods=['GET'])
    def get_friends():
        """
        Return a representation of the collection of friend resources.
        
        Returns:
            A flask.Response object.
        """
        return jsonify({"friends": datastore.friends})
    ```
- There is a lot going on here. So let's take it line by line.
    - The `@app.route()` is a **decorator**.  Decorators are used in Python 
    programs to dynamically modify an existing function, adding additional
    processing before or after the original function.
    
        > Decorators are pretty advanced so we won't really go into them 
        during this class. But, feel free to ask if you really want to know ;)
        
    - The `route` decorator connects your function to a
    URL and one or more HTTP methods.  Whenever the specified URL is called
    on your API with one of the specified methods, your function will be called.
        - In this case, it is connecting incoming requests to 
        `http://127.0.0.1:5000/api/v1/friends` using the `GET` to this function. 
        
    - You're familiar with the function definition statement and the docstring 
    by now, but what is `jsonify` doing?
        - You can guess from the docstring that it returns a flask.Response
        object - which ultimately becomes the HTTP response from your
        API to the client.
        - In particular, it creates a response object with a JSON payload,
        sets the `content-type` header to `application/json` and sets to the
        status code of the response to `200 OK`.
        - You can see from the example that you can pass a dictionary to it,
        which will then become the JSON payload.
        
        > ![Extra Info](../images/reminder.png) You can always use `help`
        > on the method, look it up in PyCharm's inline help, or in the 
        > [Flask](http://flask.pocoo.org/docs/0.10/api/#flask.json.jsonify) 
        > documentation.
    
## There Is No Secret Ingredient: Testing
In order to test your API, you'll need two terminal windows open with active
SSH sessions in your Vagrant VM.  
- For Mac users, this should be relatively easy.  You can open multiple tabs 
in the default `terminal` application, or use the excellent iTerm2 for even
better options.

- Windows users, time for a little bit more pain.  You'll need to have two 
separate instances of Git Bash running and just position the windows next to 
each other.  It might not be very clear on how to start multiple instances of 
the same application in any given version of windows, so this might take a bit
to get setup.

Once you have two SSH terminal sessions open do the following:
- In the first terminal session make sure that you've gone to `level-4` and
then executed `cd` into your subdirectory.

- From here, you can execute `python run_server.py`.  This will start the test 
HTTP server that is bundled with Flask and load your API into it. 
The output will look like this if everything worked correctly:

    ```bash
     * Restarting with stat
     * Debugger is active!
     * Debugger pin code: 170-875-347
    ```
    
- In your second terminal window, you can issue `curl` commands to access
various methods of your API.  Test your first method with the following command:

    ```bash
    curl 127.0.0.1:5000/api/v1/friends
    ```
  
- You should get the following response:
    
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
    
    > ![Problem Alert](../images/alert.png) Remember that both terminal 
    > sessions need to have active SSH connections to the Vagrant VM 
    > (`vagrant ssh`) for this to work correctly.