[Previous](exercise-6.md) |  [Next](exercise-8.md)
## Refactoring for DRY Compliance
Well, if you haven't Googled it by now, I'll tell you what DRY stands for:
**Don't repeat yourself.**  

Violating this principle will get your in trouble with the cool kid 
programmers in any language, not just Pythonistas.

#### Step 1: So What is Repeated in our Code?

Before we go one, let's take the duplicate code out of `create_friend` and
`fully_update_friend`.  This is the section that is common to both functions:
```python
...
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
    
for friend in datastore.friends:
    if [some_variable] == friend['id'].lower():
...
```
    
* There are basically three different things that are being done in this 
  section:
    * Verifying a JSON payload is present and correctly formed.
    * Verifying the all the required data elements are present in the payload.
    * Checking to see if an existing friend resource exists for a given `id`.
    I've indicated that the variable in the `if` statement can vary but the 
    functionality is the same.
    
* We're going to find a way to extract these bits of code into functions so 
that future maintainers of our growing codebase don't want to track us down 
and kill us.

#### Step 2: Adding a Function to See if a Friend Exists
* Open `datastore.py` and add the following function to it:
    ```python
    def existing_friend(id:str) -> dict:
        """
        Return a representation of friend resource that matches a given
        `id` if it exists.
    
        Args:
            id (str): The id value to search for a resource with.
    
        Returns:
            A dictionary representation of the friend resource or None if
            no match is found.
        """
        for friend in friends:
            if id.lower() == friend['id'].lower():
                return friend
    ```
    
    * Pretty simple right?  Check for the existence of an existing friend
    resource based on the `id` parameter and return the friend dictionary 
    if a match is found, otherwise return nothing.
    
#### Step 3: Replace Duplicate Code with `datastore.existing_friend`
* Now, let's see how we can insert this into `create_friend` and 
    `fully_update_friend`:
    
        ```python
        # inside create_friend
        
        # replace this
        for friend in datastore.friends:
            if request_payload['id'].lower() == friend['id'].lower():
                error_response = make_response(
                    jsonify(
                        {"error": "An friend resource already exists with the "
                                  "given id: {}".format(request_payload['id'])}),
                    400)
                return error_response
        
        # with this
        if datastore.existing_friend(id=request_payload['id']):
            error_response = make_response(
                jsonify(
                    {"error": "An friend resource already exists with the "
                              "given id: {}".format(request_payload['id'])}),
                400)
            return error_response
        
        ```
        
        ```python
        # Inside fully_update_friend
        
        # Replace This
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
            
        # With This
        existing_friend = datastore.existing_friend(id)
        if existing_friend:
            existing_friend.update(
                {"id": request_payload['id'],
                 "first_name": request_payload['firstName'],
                 "last_name": request_payload['lastName'],
                 "telephone": request_payload['telephone'],
                 "email": request_payload['email'],
                 "notes": request_payload['notes']})
        
            response = make_response(
                jsonify({"message": "Friend resource updated."}), 201)
            return response
        ```
        
* As an unintended bonus, we can also update `get_friend` so that it looks like
this:
    ```python
    def get_friend(id: str):
        """Return a representation of a specific friend or an error."""
    
        try:
            return jsonify(datastore.existing_friend(id))
        except TypeError:
            error_response = make_response(
                jsonify({"error": "No such friend exists."}), 404)
            return error_response
    ```
        
