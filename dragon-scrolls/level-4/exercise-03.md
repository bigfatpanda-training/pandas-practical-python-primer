[Previous](exercise-02.md) |  [Next](exercise-04.md)
## Exercise 3: Storing & Importing Friendship Information
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_02)

No API is really useful without data.  After all, it is data that we will be
retrieving, creating, updating, and deleting via an API.

We need a place to keep our data.  Later on, we'll use a database for this.
Right now however, we'll just use another module.

### There Is No Secret Ingredient
- Create a new module in your `friends_api` package called `datastore.py`.
- Add the following `dict` object to the file.  This will be your initial 
set of friends.  Congratulations:

    ```python
    friends = [
        {
            "id": "BFP",
            "first_name": "Big Fat",
            "last_name": "Panda",
            "telephone": "574-213-0726",
            "email": "mike@eikonomega.com",
            "notes": "My bestest friend in all the world."
        },
        {
            "id": "VinDi",
            "first_name": "Vin",
            "last_name": "Diesel",
            "telephone": "I-HIT-PEOPLE",
            "email": "vdiesel4@supercool.edu",
            "notes": "Really annoying guy.  Will never amount to anything."
        }
    ]
    ```
    
- Update `friends.py` to import the `datastore` module:


#### Step 2: Access `datastore.friends` from `api.py`
- How do we access data from one module in another module?  We `import` it!
- Add the following to `api.py`: 
    ```python
    from flask import Flask, jsonify
    
    from friends_api import datastore
    ...
    ```
- Drop to the command line and run `python -i trainee_friends_api.api` and 
see if you can access `datastore.friends`.  
    - This should break with a 
    
    > ![alert](../images/alert.png) If you prefer the default `python` 
    interpreter, don't forget to add the `-m' option.  If you don't, your 
    program won't handle the import statements correctly and will break.

    

   
