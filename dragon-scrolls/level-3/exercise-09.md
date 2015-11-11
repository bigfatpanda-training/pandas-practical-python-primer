[Previous](exercise-7.md) |  [Next](exercise-9.md)
### Step 8: Reading Data with Box API SDK 
Let's pull data out of our accounts using the Box API/SDK.

* Obtain information about your user account in Box.  Inspect the resulting
object with [`dir()`](https://docs.python.org/3/library/functions.html?highlight=vars#dir), [`vars()`](https://docs.python.org/3/library/functions.html?highlight=vars#vars), and `help()`.
    ```python
    ...
    box_client = boxsdk.Client(oauth)

    # Obtain Box User Info
    box_user_info = box_client.user(user_id='me').get()
    ...
    ```

* Now let's get some basic information about what is in our Box account.  We'll 
start by pulling back the root folder of the account and seeing what's inside.
Just like before, we inspect this object to see what attributes and methods it
has available to us.

    ```python
    ...
    # Obtain Box User Info
    box_user_info = box_client.user(user_id='me').get()

    # Obtain Root Folder Handle and Info
    root_folder = box_client.folder(folder_id='0').get()
    ...
    ```
    
* Of interest is the `root_folder.get_items()` method which returns a list of
object handles which each have an `id` and `type` attributes.

    ```python
    ...
    # Obtain Root Folder Handle and Info
    root_folder = box_client.folder(folder_id='0').get()

    
    # Root Folder Items
    items = box_client.folder(folder_id='0').get_items(limit=100, offset=0)

    for item in items:
        print(item.type, item.id)
    ...
    ```
    
*  We can use the `type` and `id` attributes of each item to actually retrieve
the objects from the API.  Let's do that all files it our `items` list.

    ```python
    ...
    # Root Folder Items
    items = box_client.folder(folder_id='0').get_items(limit=100, offset=0)

    for item in items:
        if item.type == "file":
            api_response = json.loads(
                box_client.file(file_id=item.id).get().content().decode())
            print("-" * 50)
            print("File Name: {}".format(item.name))
            print("File Content: {}".format(api_response['atext']['text']))
    ...
    ```
    
    * Make sure to talk about the wicked method chaining here.