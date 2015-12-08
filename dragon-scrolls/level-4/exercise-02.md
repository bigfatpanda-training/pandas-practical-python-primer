[Previous](exercise-01.md) |  [Next](exercise-03.md)
## Exercise 2: A Barebones Flask API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_01)

In this exercise, you will create a Flask API that does... NOTHING! Yeah!
Actually, that's a bit of a lie.  It will actually do a lot of things, but
won't have any of the functionality that we'll be creating as we continue.
    
### There Is No Secret Ingredient
- In your `friends_api` package, create a file called `friends.py` with 
the following content:

    ```python
    from flask import Flask, jsonify
    
    app = Flask(__name__)
    ```   
    
    - Can you remember how the special module property `__name__` works?  You
    can see that it is being used as a parameter for the Flask object
    constructor.
    
- Drop to the command line and start your API by executing the `run_server.py`
script.  You should see something like this:

    ```bash
    >>> python run_server.py
    * Restarting with stat
    * Debugger is active!
    * Debugger pin code: 981-417-957
    ```
    
- Open another terminal session to your Vagrant machine and hit your 
API and see what happens: `curl http://127.0.0.1:5000`.  You should
get a response back.

> ![Reminder](../images/reminder.png) Don't forget to add the module docstring.

| [Next Exercise](exercise-03.md)
