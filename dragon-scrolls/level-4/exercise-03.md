[Previous](exercise-02.md) |  [Next](exercise-04.md)
## Exercise 3: Storing & Importing Friendship Information
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_02)

No API is really useful without data.  After all, it is data that people (and
machines) retrieve, create, update, and delete via an API.

We need a place to keep our data.  Later on, we'll use a database for this.
Right now however, we'll just use another module, called `datastore`.

This will allow us to get going quickly, but also has a downside.  All
updates to our program data will only live in memory.  Whenever we restart
the API, the data will be reset to whatever is defined in the `datastore`
module.

### There Is No Secret Ingredient: A Place for Our Data
- Create a new module in your `friends_api` package called `datastore.py`.
- Add the following `dict` object to the file.  This will be your initial 
set of friends.  Congratulations:
    
    ```python
    friends = [
        {
            "id": "BFP",
            "firstName": "Big Fat",
            "lastName": "Panda",
            "telephone": "574-213-0726",
            "email": "mike@eikonomega.com",
            "notes": "My bestest friend in all the world."
        },
        {
            "id": "VinDi",
            "firstName": "Vin",
            "lastName": "Diesel",
            "telephone": "I-HIT-PEOPLE",
            "email": "vdiesel4@supercool.edu",
            "notes": "Really annoying guy.  Will never amount to anything."
        }
    ]
    ```
    
    - ![Dictionary Key Names](../images/information.png) Notice that 
    dictionary key names do **not** have to conform to PEP8 syntax rules
    for variable names. Here we are using JSON naming convention syntax, since 
    that is what we'll be interacting with in the API.
    
- Update `friends.py` to import the `datastore` module:
    
    ```python
    from flask import Flask, jsonify
    
    from friends_api import datastore
    ...
    ```

- Drop to the command line and run `python -i -m friends_api.friends` and 
see if you can access `datastore.friends`.  

    > ![New Information](../images/information.png) Up to this point in 
    > your training, you've never seen the `-m` flag used before.  You have
    > to use it when executing a package module as a script (like we are doing
    > here).  Otherwise, the `import` statements that refer to other package 
    > modules will break.  

    

   
