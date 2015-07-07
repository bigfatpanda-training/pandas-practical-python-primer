[Previous](exercise-3.md) |  [Next](exercise-5.md)
## Add HTTP POST Support to our Web Service API
In a properly designed RESTful web service/api, we create new resources using
the POST HTTP method.  It's time for us to do that for our API so that we can 
create new friend records in our datastore.

> ![Question](../images/question.png) Review: What are the other common HTTP
methods (GET, PUT, PATCH, DELETE) used for in RESTful web services/apis?

#### Step 1: Create a Function for Handling HTTP POST Requests
* Add the following function stub to `api.py` below your other functions:
    ```python
    @app.route('/api/v1/friends', methods=['POST'])
    def create_friend():
        """
        Create a new friend resource. 
        
        Utilize a JSON representation in the request object to create
        a new friend resource.
        """
        pass
    ```

* The first thing our function needs to do is get access to the 
"JSON representation in the request object" that is referenced in the 
docstring in order to construct a new friend resource.  You can do so by 
replace `pass` with the following code:

    ```python
    request_payload = request.get_json()
    ```
    * The `request` object is a globally scoped name/variable whose value is 
    always bound to the current HTTP request being handled by the program. Yes,
    that is a mouthful.
    * Because it is a globally scoped name, you can access it from within any
    function, as long as you have imported it from the `flask` library.
    
        > ![reminder](../images/reminder.png) Remember to import the `request`
        > object from the flask library.
         
* Now that you have the JSON payload, you can use it to create a new
friend resource and return a success message to the client:

    ```python
    request_payload = request.get_json()
    
    datastore.friends.append(
        {"id": request_payload['id'],
         "first_name": request_payload['firstName'],
         "last_name": request_payload['lastName'],
         "telephone": request_payload['telephone'],
         "email": request_payload['email'],
         "notes": request_payload['notes']})

    response = make_response(jsonify({"message": "Friend resource created."}),
                             201)
    return response
    ```
    
    * In this code were are using the `append` method on the `datastore.friends`
    list object to create a new friend record, which is itself a dictionary.
    * You can see how we access different parts of the `request_payload` 
    object as values in the new dictionary.
    * Finally, you can see how we use the `make_response` function to override
    the standard `200` response code with `201` which means a new resource
    was successfully created.
    
#### Step 2: Test your API
Let's take our new functionality for a test.
* From the terminal windows issue the following command: `curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'`
    
    > ![info](../images/information.png) `-X` allows you to specify which HTTP method to use.
    
    > ![info](../images/information.png) `-H` allows you to specify HTTP headers and values.
    
    > ![info](../images/information.png) `-d` allows you to specify the data to pass in the payload.
* This is the response that you should get back:
    
    ```
    {
      "message": "Friend resource created."
    }
    ```
    
#### Step 3: There Be Bugs!
If you've been following along very precisely, everything should have worked
up to this point.  However, we actually been introducing bugs into our program
along the way.  Try the following `curl` operations to see them crawl out of their 
holes:
    
    * Leave out the header that sets `content-type` to `application/json` 
    * Have a syntax error in the JSON payload.
    * Leave out the `firstName` element from the JSON payload.