[Previous](exercise-04.md) |  [Next](exercise-06.md)
## Exercise 4: Additional HTTP GET Support to your API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_04)

In this exercise you will add support for retrieving a specific friend 
resource representation from your API.

### There Is No Secret Ingredient: [GET] One Specific Friend
Add the following new function to your `friends.py` module:

```python
@app.route('/api/v1/friends/<id>', methods=['GET'])
def specific_friend(id: str):
    """
    Return a representation of a specific friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    for friend in datastore.friends:
        if friend['id'] == id:
            return jsonify(friend)

    error_response = make_response(
        jsonify(
            {"error": "No friend found with the specified identifier. "
                      "BFP is a Big Fat Panda Loser!"}), 404)
    return error_response
```

- Notice that in the `@app.route` decorator of our new function that there 
is a `<id>` added to the end of the URL.  Whenever a segment of the URL is
enclosed in `<>`, Flask will capture the that portion of the URL and 
pass it to your function as a variable named whatever was inside the `<>`. 
    - In this case, it passes `id` into our function. In a real request,
    let's say to `www.yourserver.com/api/v1/friends/BFP`, `BFP` would be
    sent to our function as the variable `id`.

- You can see here that we iterate over all the elements of 
`datastore.friends` and consider whether each one has a matching `id` 
value to what was requested.
    
- If a matching friend is found, we return just that single friend record 
to the client.

- If no matching friend is found however, we need to return a different type 
of response to the client.  In order to do this, we make use of the 
`flask.make_response` function.
    - This function allows us to take another flask.Response object as the 
    first parameter, and then modify its status code with the second parameter.
    - In this case, you can see that we pass a JSON-based response object 
    created by `jsonify` into `make_response` as its first argument.  
    - Then as the second parameter, we pass a override status code, that will
    replace the default `200 OK` status code on the `jsonify` response object.
- Finally, we return the modified reponse object.
    
> ![Don't Forget](../images/checklist.png) Make sure that you update your 
`from flask import ...` statement to include `make_response` or your program
will fail with an undefined NameError.

> ![Question](../images/question.png) What are we changing the HTTP status code
> to?  Why is that important?

### There Is No Secret Ingredient: Testing
- Drop to the command-line and try to access your new method: 
`curl 127.0.0.1:5000/api/v1/friends/VinDi`.  You should get the following
output:
    
    ```JSON
    {
      "email": "vdiesel4@supercool.edu",
      "first_name": "Vin",
      "id": "VinDi",
      "last_name": "Diesel",
      "notes": "Really annoying guy.  Will never amount to anything.",
      "telephone": "I-HIT-PEOPLE"
    }
    ```

> ![Alert](../images/alert.png) We've introduced a bug here that might not be
> be immediately obvious.  What happens when we query for `BFP`?  What about
> `bfp`?  How might we account for this?

