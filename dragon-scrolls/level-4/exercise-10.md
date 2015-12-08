[Previous](exercise-7.md) |  [Next](exercise-9.md)
## Adding HTTP DELETE Support in our Web Service API
OK. This one is going to be easy!  Let's add the ability to delete our friends!

#### Step 1: Create a `destroy_friend` Function
```python
@app.route('/api/v1/friends/<id>', methods=['DELETE'])
def destroy_friend(id: str):
    """
    Delete a specific friend resource or return an error.

    Returns
        HTTP Response (200): Friend resource deleted.
        HTTP Response (404): No matching existing resource to update.
    """
    try:
        existing_friend = datastore.existing_friend(id)
        datastore.friends.remove(existing_friend)
    except ValueError:
        error_response = make_response(
            jsonify({"error": "No such friend exists."}), 404)
        return error_response
    
    return jsonify({"message": "Friend resource removed."})

```

* This one is pretty simple!  If was our `datastore.existing_friend` function
to get a reference to our existing friend (if it exists) or return `None`.
  
* We then try to delete the friend via the 
`datastore.friends.remove(existing_friend)` statement.
    * If the value of `existing_friend` is `None` a `ValueError` exception
    will be raised and an error response generated for the client.
    * Otherwise, the friend resource has been deleted and a success message
    will be given to the client.

        > ![info](../images/information.png) The documentation on the `list.remove`
        method is not the clearest. Basically, it finds the first location 
        (index) of a given value in a list and deletes it.  It even works when 
        value we are deleting is a dictionary.  **Cool!**
        
> ![info](../images/information.png) You might be wondering why the final 
`return` statement wasn't included in the `try` block.  The answer is that 
`try` blocks should only contain the code that you expect an exception to be
raised from.  Otherwise, you might accidentally "handle" an exception that you
didn't mean to.

#### Step 2: Test API Handling of `DELETE` Requests
Let's make sure that the API is operating as expected.
    
* Delete your BFP friend and make sure you get the correct output: 
```bash
> curl http://127.0.0.1:5000/api/v1/friends/BFP -X DELETE

{
  "message": "Friend resource removed."
}
```
* Pull back a list of your friends to verify that `BFP` is no longer there: `curl http://127.0.0.1:5000/api/v1/friends`
* Make sure you can't delete a non-existent friend resource:
```bash
> curl curl http://127.0.0.1:5000/api/v1/friends/nobody -X DELETE

{
  "error": "No such friend exists."
}

| [Next Exercise](exercise-11.md)
    
       
        
