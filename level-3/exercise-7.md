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
        
    > ![checklist](../images/reminder.png) Notice that we didn't use and `if`
    > statement here like we did in the other functions.  Generally, Pythonistas
    > use a EAFP (easier to ask forgiveness than permission) coding style rather
    > than a LBYL (look before you leap) style.  
    > 
    > This style is characterized by the use of `try/except` blocks rather 
    > than if statements.  We could have converted the `if` statements in 
    > `create_friend` and `fully_update_friend` but I though this was a better
    > place to do so because the logic is much simplier.  
    >
    > Either method will work, but one is considered more Pythonic is most
    > circumstances.
    
#### Step 3: Create a Function that Ensures JSON Payloads are Present and Valid
Next, let's turn our attention to the following section of duplicated code
that handles requests from users with missing headers and missing/invalid 
JSON payloads:  
```python
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
                          "included in your request and that you've "
                          "specified a payload."}),
        400)
    return error_response
```

* Create a new moduled call `api_helpers.py`.
* Inside this new module add the following:

    ```python
    """
    This module provides functions that are commonly used by various
    members of the api.py module.
    """
    
    from werkzeug.exceptions import BadRequest
    
    
    def json_payload(request) -> dict:
        """
        Verify that a flask.request object has a JSON payload and
        that it does not contain syntax errors.
    
        Args:
            request (flask.request): A request object that you want to
                verify has a valid JSON payload.
    
        Raises:
            ValueError: If the incoming request object is either missing
                a JSON payload or has one with syntax errors.
        """
        try:
            request_payload = request.get_json()
        except BadRequest:
            raise ValueError("JSON payload contains syntax errors. Please "
                             "fix and try again.")
    
        if request_payload is None:
            raise ValueError("No JSON payload present.  Make sure that "
                             "appropriate `content-type` header is "
                             "included in your request and that you've "
                             "specified a payload.")
    
        return request_payload
    ```
    
    * This module contains the essential logic from our previously duplicated
    code.  In short, if any error is encounter based on the content of the 
    incoming request, a ValueError is raised.  Otherwise the validated
    JSON payload is returned.
    
    
* Replace the duplicated code in `create_friend` and `fully_update_friend` with
this:
    
    ```python
    try:
        request_payload = api_helpers.json_payload(request)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response
    ```
    
    >  ![alert]("../images/alert.png") Don't forget to import `api_helpers` 
    into `api.py` or this won't work. PyCharm should alert you to this problem
    via a red squiggly line.
    
#### Step 4: Create a Function that Validates JSON Payloads have all Required Elements
As the last step in this exercise, we need to extract this final piece of 
duplicate code into a function:

```python
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

* Create another function in `api_helpers.py` called `verify_required_data_present`
    ```python
    def verify_required_data_present(request_payload: dict, required_elements: set):
        """
        Verify that a request_payload has all the keys indicated
        in required_elements.
    
        Args:
            request_payload (dict): A set of request_payload to evaluate.
            required_elements (set): The names of keys that must be present
                in request_payload.
    
        Raises:
            ValueError: If any of the names in required_elements is not a
                member of request_payload.keys()
        """
    
        if not required_elements.issubset(request_payload.keys()):
            raise ValueError(
                "Missing required payload elements. "
                "The following elements are "
                "required: {}".format(required_elements))
    ```
    
    * Notice that this function raises a `ValueError` exception when the
    specified `request_payload` value doesn't have all the required data elements.
    This is useful because it is the same error that is raised in our previously
    added function, which means it can be handled by the same `try/except` block
    in the calling functions.
    
* Replace the duplicate code in `create_friend` and `fully_update_friend` by
augmenting the code we added in the last step to include a call to 
`api_helpers.verify_required_data_present` 
in the `try` block so that it looks like this:
    
    ```python
    try:
        json_payload = api_helpers.json_payload(request)
        api_helpers.verify_required_data_present(
            request_payload=json_payload,
            required_elements=FRIEND_RESOURCE_ELEMENTS)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response
    ```
    
    > ![question](../images/question.png) Is PyCharm complaining about 
    > `FRIEND_RESOURCE_ELEMENTS`?  That's good because we haven't defined it yet.
    > 
    > Notice that when we created this last function and eliminate the duplicate
    > code we no longer had a place where the required payload elements were
    > defined (`id`, `firstName`, `lastName`, etc.).
    >
    > You can tell from the syntax of `FRIEND_RESOURCE_ELEMENTS` that I created
    > a constant to hold the set of values previously assigned to 
    > `required_data_elements`.  Make sure you do that (at the top of your file)
    > as well if you want the program to work.
    
* You might be wondering to yourself, _why are there two separate functions in
`api_helpers.py` since they are always both used together?  And why not just
defined `required_data_elements` in that one function instead of defining it
as a constant?_
 
* The answer is that I know that future API functionality (like supporting `PATCH`)
would require these functions to be separated because while you would need to ensure
that a valid JSON payload was given (1st function), it wouldn't need to have all
the elements required checked for by our second function.  For the same reason
I defined `FRIEND_RESOURCE_ELEMENTS` outside of a function, so that it could be
used even when the `verify_required_data_present`.
