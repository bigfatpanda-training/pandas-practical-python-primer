[Previous](exercise-5.md) |  [Next](exercise-7.md)
## Adding HTTP PUT Support in our Web Service API
I hope that you are starting to get the hang of adding functionality to your
API by now.  We're going to finish off this session's training by adding
the ability to replace and delete our friends (after all, haven't we all wanted
to change or delete or friends from time to time?).

We will not be implementing the `PATCH` method due to a lack of time, but doing
so would be an excellent way to solidify your knowledge and gain some more
experience.

#### Step 1: Create a `fully_update_friend` Function with the Appropriate URL Route
```python
@app.route('/api/v1/friends/<id>', methods=['PUT'])
def fully_update_friend(id: str):
    """
    Update all aspects of a specific friend or return an error.

    Use a JSON representation to fully update an existing friend
    resource.

    Returns
        HTTP Response (200): If an existing resource is successfully updated.
        HTTP Response (400): No JSON payload, bad syntax, or missing data.
        HTTP Response (404): No matching existing resource to update.
    """
    pass
```

Here's the stub for our new function.  Notice that we are using the same
URL template as we did for `get_friend`.  We've only modified the method
on the `app.route` decorator.  `PUT` requests will route to this new method, 
while `GET` requests to the same url will route to `get_friend`.  Pretty cool!

#### Step 2: Add the Functionality Borrowed from `create_friend`
Much of the logic that we'll need for this function is the same as we used
in our `create_friend` method that handled `POST` requests.  So let's start
by copying that code over into our new function.

```python
@app.route('/api/v1/friends/<id>', methods=['PUT'])
def fully_update_friend(id: str):
    """
    Update all aspects of a specific friend or return an error.

    Use a JSON representation to fully update an existing friend
    resource.

    Returns
        HTTP Response (200): If an existing resource is successfully updated.
        HTTP Response (400): No JSON payload, bad syntax, or missing data.
        HTTP Response (404): No matching existing resource to update.
    """
    try:
        request_payload = request.get_json()
    except BadRequest:
        error_response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. Please "
                              "fix and try again."}),
            400)
        return error_response

    if request_payload is None:
        error_response = make_response(
            jsonify({"error": "No JSON payload present.  Make sure that "
                              "appropriate `content-type` header is "
                              "included in your request."}),
            400)
        return error_response

    required_data_elements = {
        "id", "firstName", "lastName", "telephone", "email", "notes"}

    if not required_data_elements.issubset(request_payload.keys()):
        error_response = make_response(
            jsonify(
                {"error": "Missing required payload elements. "
                          "The following elements are "
                          "required: {}".format(required_data_elements)}),
            400)
        return error_response
```

* Just like before, we have to verify that we don't have a missing payload, 
JSON syntax errors, or missing data elements.  You can see that we added those
checks again here?

> ![alert](../images/alert.png) Does some seem wrong to you?  It should! We're
violating the DRY principle of good programming.  Some Pythonista is screaming
in horror at this very moment! Any guesses about what the
DRY principle is?  


#### Step 3: Add Unique Code Needed for Handling PUT Requests
Add the following code to complete our `fully_update_friend` function: 
```python
...
for friend in datastore.friends:
    if id.lower() == friend['id'].lower():
        friend.update(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})

        response = make_response(
            jsonify({"message": "Friend resource updated."}), 201)
        return response

error_response = make_response(
    jsonify(
        {"error": "No friend resource exists that matches "
                  "the given id: {}".format(request_payload['id'])}),
    404)
return error_response
...
```

* In our `create_friend` function, we looped through our existing list of 
friends to make sure that another friend with a given id **did not** already
exist. This time, we are doing the opposite - ensuring that there is an 
existing friend with the specified `id` so that we can update it.

    * If a match is found, we update the existing friend entry with the new
    values from the payload.
    
        > ![info](../images/information.png) The `dict.update` method updates
        > a dictionary object with the keys/values of another object.  You
        > can see the details of how this works in the 
        > [Python documentation.](https://docs.python.org/3.5/library/stdtypes.html#dict.update)
    
    * If not match is found, we return an 404 response indicating to the user
    that no existing friend resource can be found to update.
    
    > ![reminder](../images/reminder.png) Notice that there is a slight 
    > difference in the `if` statements between the two functions.  In 
    > `create_friend` the statement references `request_payload['id']` but here
    > we reference the function parameter `id` in the comparison.
    >
    > Remember that when dealing with individual resources, the URL, not the
    > payload indicates which resource to operate on.  This allows us to even
    > change the `id` values of existing friend resources.  I'll let you decide
    > if this is a bug or a feature. 
    
#### Step 4: Testing HTTP PUT Requests
Let's verify that our new code works as expected.  Here are some tests and what
you should get back from each command:
* Try to update the `BFP` friend resource:
    
    ```bash
    > curl 127.0.0.1:5000/api/v1/friends/bfp -X PUT -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "message": "Friend resource updated."
    }
    ```

* Make a call without the `content-type` header:

    ```bash
    > curl 127.0.0.1:5000/api/v1/friends/bfp -X PUT -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "error": "No JSON payload present.  Make sure that appropriate 
      `content-type` header is included in your request and that you've 
       specified a payload."
    }
    ```
    
* Make a call with a syntax error:
    
    ```bash
    > curl 127.0.0.1:5000/api/v1/friends/bfp -X PUT -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat" "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "error": "JSON payload contains syntax errors. Please fix and try again."
    }
    ```
    
* Make a call with a missing payload element:

    ```bash
    > curl 127.0.0.1:5000/api/v1/friends/bfp -X PUT -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "error": "Missing required payload elements. The following elements are 
      required: {'email', 'telephone', 'notes', 'id', 'firstName', 'lastName'}"
    }
    
    
    ```
    
| [Next Exercise](exercise-09.md)


       
        
