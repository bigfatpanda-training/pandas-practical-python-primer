[Previous](exercise-08.md) |  [Next](exercise-10.md)
## Adding HTTP DELETE Support in our Web Service API
OK. This one is going to be easy!  Let's add the ability to delete our friends!

### There Is No Secret Ingredient: Create `destroy_friend` Functions
```python
# friends.py
@app.route('/api/v1/friends/<id>', methods=['DELETE'])
def destroy_friend(id: str):
    """
    Delete a specific friend resource or return an error.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    try:
        datastore.destroy_friend(id)
    except ValueError as error:
        response = make_response(jsonify({"error": str(error)}), 400)
        return response

    return jsonify({"message": "Friend resource removed."})

# datastore.py
def destroy_friend(id: str):
    """
    Remove an existing friend entry from our datastore of friends.

    Args:
        id: The id value of the friend to delete.

    Returns:
        ValueError: If the `id` parameter doesn't match any existing
        friend entries in our datastore.

    """
    for friend in friends:
        if id.lower() == friend['id'].lower():
            friends.remove(friend)
            return 

    raise ValueError("No existing friend was found matching id: {}".format(id))
```

### There Is No Secret Ingredient: Testing
- Delete your BFP friend and make sure you get the correct output: 

    ```bash
    >>> curl http://127.0.0.1:5000/api/v1/friends/BFP -X DELETE
    {
      "message": "Friend resource removed."
    }
    ```

- Pull back a list of your friends to verify that `BFP` is no longer there: `curl http://127.0.0.1:5000/api/v1/friends`
- Make sure you can't delete a non-existent friend resource:
    
    ```bash
    >>> curl http://127.0.0.1:5000/api/v1/friends/nobody -X DELETE
    {
      "error": "No existing friend was found matching id: nobody"
    }
| [Next Exercise](exercise-10.md)
    
       
        
