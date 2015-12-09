[Previous](exercise-07.md) |  [Next](exercise-09.md)
## Adding HTTP PATCH Support in our Web Service API
I hope that you are starting to get the hang of adding functionality to your
API by now.  In this exercise, we'll be adding the ability to update
existing friend resources.

### There Is No Secret Ingredient: Creating a `update_friend` function in 
`friends` and `datastore` modules.

Here's what the functions should look like:

```python
# friends.py
@app.route('/api/v1/friends/<id>', methods=['PATCH'])
def update_friend(id: str) -> Response:
    """
    Update an existing friend resource.

    Utilize a JSON representation/payload in the request object to
    updated an existing friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    try:
        request_payload = request.get_json()
    except BadRequest as error:
        response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. "
                              "Please fix and try again."}),
            400)
        return response

    try:
        datastore.update_friend(id, request_payload)
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}),
            400)
        return response

    response = make_response(
        jsonify({"message": "Friend resource updated."}), 201)
    return response
    
# datastore.py
def update_friend(id: str, data: dict):
    """
    Update an existing friend entry is our datastore of friends.

    Args:
        data: A dictionary of data to update an existing friend entry with.

    Raises:
        ValueError: If data is None or if no matching friend entry is found.
    """
    if data is None:
        raise ValueError(
            "`None` was received when a dict was expected during "
            "the attempt to update an existing friend resource.")

    for friend in friends:
        if id.lower() == friend['id'].lower():
            friend.update(data)
            return

    raise ValueError("No existing friend was found matching id: {}".format(id))
```

- Notice how similar `friends.update_friend` and `friends.create_friend` are.
The only real differences are in the `@app.route` decorator and the call to
`datastore.update_friend`.
    - In the decorator, we are using the same URL template as we did for 
    `specific_friend`.  We've modified the `methods` parameter to indicate
    that the decorated function should handle `PATCH` HTTP requests. PATCH` 
    requests will route to this new method, while `GET` requests to the 
    same url will route to `specific_friend`.  Pretty cool!
    - Also notice that we are also capturing the `<id>` portion of the url and
    passing it `datastore.update_friend`.

- There is also a significant degree of crossover between 
`datastore.update_friend` and `datastore.create_friend`.
    - We don't check to see if all the elements of a new friend entry are in 
    the payload.  This is unnecessary because the nature of a `PATCH` update
    is to allow for variable updates of an existing resource.  Requiring that
    all data elements of a record be present in the request would mean that
    we would only allow full updates of existing resources.

    - Instead of appending a new record to the `friends` list, we search for
    a matching record and then use the `dict.update` method to update the
    it with the JSON payload from the HTTP request.
    
    - If no matching record is found, we raise a `ValueError` exception.
    
    > ![Extra Info](../images/information.png) The `update` method of `dict`
    > objects can take another `dict` as an argument.  If matching keys are
    > found on two dictionary objects, the values from the 2nd dictionary replace
    > the values of the first dictionary for the corresponding key.  If new
    > keys are present in the second dictionary, these are added to the first
    > dictionary with their corresponding values.
    >
    > Further Reading(https://docs.python.org/3.5/library/stdtypes.html#dict.update)

    
### There Is No Secret Ingredient: Testing
Let's verify that our new code works as expected.  Here are some tests and what
you should get back from each command:

* Try to update the `BFP` friend resource:
    
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'  
    {
      "message": "Friend resource updated."
    }
    ```

* Make a call without the `content-type` header:

    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    {
      "error": "No JSON payload present.  Make sure that appropriate 
      `content-type` header is included in your request and that you've 
       specified a payload."
    }
    ```
    
* Make a call with a syntax error: 
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat" "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "error": "JSON payload contains syntax errors. Please fix and try again."
    }
    ```
        
| [Next Exercise](exercise-09.md)


       
        
