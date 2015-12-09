[Previous](exercise-10.md)
## Exercise 11: Moving to a Persistent Datastore: Part 2
Now that we've created our database and a series of functions to interact with 
it, we need to incorporate that in the various functions of `api.py`. 

### Step 1: Make a Datastore Connection Available to `friends.py` Functions
Add the following code just after your `import` statements:
    
    ```python
    @app.before_request
    def connect_to_datastore():
        """
        Establish a connection to the store for each request.
    
        Make the connection available on Flask's special 'g' object.
        """
        g.datastore = Datastore()
    
    
    @app.teardown_request
    def disconnect_from_datastore(exception):
        """
        Close the connection to the datastore after each request.
        """
        del g.datastore
    ```
    
- Don't forget that you'll also need to update your import statements
so that `g` and `Datastore` are valid names:

    ```python
    from flask import Flask, jsonify, make_response, request, Response, g
    from werkzeug.exceptions import BadRequest
    
    from friends_api.datastore import Datastore
    ```

- The decorators `@app.before_request` and `@app.teardown_request` can be 
applied to any function that you want to execute before and after every
incoming request is processed by of our other functions.

- We're going to use these methods to create destroy instances of our 
`Datastore` class that we'll need to perform database operations.  We destroy
 them at the end of each request to ensure than database connections are
 being released.

- We attach the connection to a special flask object simply (and unfortunately)
called `g`.  This special object holds data that only persists for a 
single request lifecycle and allows multiple functions/modules 
access to shared data needed for request processing.

### Step 2: Renovate `friends.py`
Now we need to make updates to the functions of `friends.py` to use
our `Datastore` object that is attached to the `g` object.

- Update `friends()`:

    ```python
    @app.route('/api/v1/friends', methods=['GET'])
    def friends() -> Response:
        """
        Return a representation of the collection of friend resources.
    
        Returns:
            A flask.Response object.
        """
        friends_list = g.datastore.friends()
        return jsonify({"friends": friends_list})
    ```
    
- Update `specific_friend()`:

    ```python
    @app.route('/api/v1/friends/<id>', methods=['GET'])
    def specific_friend(id: str) -> Response:
        """
        Return a representation of a specific friend resource.
    
        Args:
            id: The unique ID value of a given friend.
    
        Returns:
            A flask.Response object.
        """
        friend = g.datastore.friend(id)
        if friend:
            return jsonify(friend)
        else:
            response = make_response(
                jsonify({"error": "You have no friends.  LOSER."}), 404)
            return response
    ```
    
- Update `create_friend()`:

    ```python
    def create_friend() -> Response:
        """
        Create a new friend resource.
    
        Utilize a JSON representation/payload in the request object to
        create a new friend resource.
    
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
            g.datastore.create_friend(request_payload)
        except ValueError as error:
            response = make_response(
                jsonify({"error": str(error)}),
                400)
            return response
    
        response = make_response(
            jsonify({"message": "Friend resource created."}), 201)
        return response
    ```
    
- Update `update_friend()`:

    ```python
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
            g.datastore.update_friend(id, request_payload)
        except ValueError as error:
            response = make_response(jsonify({"error": str(error)}), 400)
            return response
    
        response = make_response(
            jsonify({"message": "Friend resource updated."}), 201)
        return response
    ```
    
- Update `destroy_friend()`:

    ```python
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
            g.datastore.destroy_friend(id)
        except ValueError as error:
            response = make_response(jsonify({"error": str(error)}), 400)
            return response
    
        return jsonify({"message": "Friend resource removed."})
    ```