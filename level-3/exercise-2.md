[Previous](readme.md) |  [Next](exercise-2.md)
## Storing & Importing Friendship Information
#### Step 1: Add some information on your friends to `datastore.py`
* Since we don't have a database to store our program data.  We're going to 
keep it in a dictionary for the time being.  Add the following to `datastore.py`:
    
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
* We'll access and edit this list via our API to create/modify/delete our friends!
* Don't forget to add a docstring to the file.  Hopefully PyCharm will remind
you that this is currently missing.


#### Step 2: Access `datastore.friends` from `api.py`
* How do we access data from one module in another module?  We `import` it!
* Add the following to `api.py`: 
    ```python
    from flask import Flask, jsonify
    
    from trainee_friends_api import datastore
    ...
    ```
* Drop to the command line and run `ipython -i trainee_friends_api.api` and 
see if you can access `datastore.friends`

    ![alert](../images/alert.png) If you prefer the default `python` 
    interpreter, don't forget to add the `-m' option.  If you don't, your 
    program won't handle the import statements correctly and will break.

    

   
