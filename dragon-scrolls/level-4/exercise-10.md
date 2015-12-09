[Previous](exercise-09.md) |  [Next](exercise-11.md)
## Moving to a Persistent Datastore: Part 1
Now that we've created a fully functional Web API, it's time to move it towards
a production ready state.  One of the pieces needed for that is to have a 
persistent datastore that doesn't get wiped out each time we restart out 
program.

We'll be using the [SQLite](https://www.sqlite.org/) database because it is 
extremely easy to start using in Python.  You could however use almost any
SQL or noSQL datastore as there are 3rd party libraries available for almost
every conceivable option.

### Step 1: Install SQLite
To install sqllite, execute the following command inside your Vagrant 
SSH session: `sudo apt-get install sqlite3` 

### Step 2: Create a SQLite Datastore
Inside your class folder (which you can get to by typing `level-4` and the 
terminal window) you see a file called `datastore_setup.sql`. We'll use this
file to create our datastore.  Feel free to examine it's contents inside of 
PyCharm.
    
- To create the datastore, execute this command: `sqlite3 /tmp/friends.db < datastore_setup.sql`
- The datastore will live at `/tmp/friends.db`.

### Step 3: Renovate `datastore.py`
Previously, this module held the list of our friends and a functions
for interacting with that list. We're going to get rid of that list now
and create a class with methods to interact with our database.

- Update the module docstring and `sqllite` import statement.
    ```python
    """
    This modules provides functions for creating, updating, and deleting
    friend records from our database.
    """
    
    import sqlite3
    ```

    > ![info](../images/information.png) Note that `sqllite` module is 
    actually part of the standard library.  No need to download additional 
    libraries.
    
    
- Create a `Datastore` class that will hold a connection to our SQLite 
database and our methods:

    ```python
    class Datastore:
        """
        Provides an interface to an SQLite database and associated methods.
        """
    
        def __init__(self):
            self.connection = sqlite3.connect("/tmp/friends.db")

    ```
    - You can see in our constructor/initialization method (`__init__`) we
    set the instance attribute `self.connection` to be a connection to our
    SQLite database.
    
- Add a class method that returns all rows from the `friends` table of our
database:

    ```python
    def friends(self) -> dict:
        """
        Return a representation of all rows in the friends table.
    
        Returns
            A JSON ready dictionary representing all rows of the friends table.
        """
    cursor = ds_connection.execute(
        'select id, firstName, lastName, telephone, email, notes '
        'from friends')

    friends_collection = list()
    for friend_row in cursor.fetchall():
        friends_collection.append(
            {"id": friend_row[0],
             "firstName": friend_row[1],
             "lastName": friend_row[2],
             "telephone": friend_row[3],
             "email": friend_row[4],
             "notes": friend_row[5]})

    return friends_collection
    ```
    
    - Connections to SQLlite databases have a method called `execute` which allows
    you to, unsurprising, execute SQL statements against the datastore.  You
    can see here that we are doing a `select` statement to get data on all
    the rows in the friends table.
        
        - Generally speaking, database providers that follow the Python 
        database standard would all have this method on their connection
        objects.
    
    - Because our data is no longer automatically structured for us the 
    way it was before in `datastore.friends`, an empty list is created and 
    populated with entries in a format that the API will be able to return as 
    JSON. 
    
- Convert our `friend` function to a method and makes some changes to it:
    ```python
    def friend(self, id: str) -> dict:
        """
        Obtain a specific friend record and return a representation of it.

        Args:
            id (str): An `id` value which will be used to find a specific
                datastore row.

        Returns
            A JSON ready dictionary representing a specific
            row of the friends table.
        """
        cursor = self.connection.execute(
            'select id, firstName, lastName, telephone, email, notes '
            'from friends where lower(id) = ?',
            [id.lower()])

        friend_row = cursor.fetchone()

        if friend_row:
            return {
                "id": friend_row[0],
                "firstName": friend_row[1],
                "lastName": friend_row[2],
                "telephone": friend_row[3],
                "email": friend_row[4],
                "notes": friend_row[5]}
    ```
    
    - This function is similiar to the previous one.  There are a few differences however:
        - The `select` statement uses the function parameter `id` to lookup a 
        specific friend.  Much our old `datastore.existing_friend` function did.
            
            - Notice that a non-standard form of string interpolation is used 
            here (no use of the `format` method).  Instead `?` symbols in the
            SQL statement are replaced by values of a list given as the second 
            parameter of the method call.
            
                > ![alert]("../images/alert.png") This non-standard way of 
                string interpolation is actually a security feature.  Behind
                the scenes, the sqllite library inspects the values of the list
                to ensure that your code doesn't become a victim of SQL injection.
                
        - Since only one row should be returned from the `execute` call, only
        one record is pulled out from resulting `cursor` object.
        
        - A single dictionary is returned instead of a list of dictionaries.  
        
- Convert and modify your `create_friend` function:
    
    ```python
    def create_friend(self, data: dict):
        """
        Create a new friend record in our database.

        Args:
            data: A dictionary of data for our new friend.  Must have
                the following elements: ['id', 'firstName', 'lastName',
                'telephone', 'email', 'notes']

        Raises:
            ValueError: If data is None, doesn't contain all required
                elements, or an existing record with the same id exists
                in the friends table.
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new friend resource.")

        required_elements = {"id", "firstName", "lastName", "telephone",
                             "email", "notes"}

        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))

        if not self.friend(data['id']):
            raise ValueError(
                "A friend already exists with the `id` specified: {}".format(
                    data['id']))

        self.connection.execute(
            'insert into friends (id, firstName, lastName, telephone, email, notes) '
            'values (?, ?, ?, ?, ?, ?)',
            [data['id'],
             data['firstName'],
             data['lastName'],
             data['telephone'],
             data['email'],
             data['notes']])
        self.connection.commit()
    ```
    - This function performs an SQL `insert` statement, which is used to create
    new rows in a given table. 
    
    - It also uses the `commit` method of the database connection object. 
    This effectively makes your new row permanent in the datastore.
    
- Convert and modify your `update_friend` function:
    
    ```python
    def update_friend(self, id: str, data: dict):
        """
        Update an existing friend entry is our database.
    
        Args:
            id: The id value of the friend to update.
            data: A dictionary of data to update an existing friend entry with.
    
        Raises:
            ValueError: If data is None or if not matching friend entry is found.
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to update an existing friend resource.")
        
        required_elements = {"id", "firstName", "lastName", "telephone",
                             "email", "notes"}

        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))
    
        if not self.friend(id):
            raise ValueError(
                "No existing friend was found matching id: {}".format(id))
    
        self.connection.execute(
            "UPDATE friends "
            "SET id=?, firstName=?, lastName=?, telephone=?, email=?, notes=? "
            "WHERE lower(id) = ?",
            [data['id'],
             data['firstName'],
             data['lastName'],
             data['telephone'],
             data['email'],
             data['notes'],
             data['id'].lower()])
        self.connection.commit()
    ```
    
    - This function is almost identical to the previous one except:
        - It uses the sql `update` command and associated syntax.
        
        - `entry_data['id']` is injected into the statement twice, both as a 
        value to update and as a key for the `WHERE` clause of the statement 
        to lookup the existing entry.
        
- Convert and modify your `destroy_friend` function:
    ```python
    def destroy_friend(self, id: str):
        """
        Remove an existing friend entry from our datastore of friends.

        Args:
            id: The id value of the friend to delete.

        Returns:
            ValueError: If the `id` parameter doesn't match any existing
            friend records in our database.

        """
        if self.friend(id):
            cursor = self.connection.execute(
            'DELETE  '
            'from friends where lower(id) = ?',
            [id.lower()])

            if not cursor.rowcount:
                raise ValueError()
            else:
                self.connection.commit()
        else:
            raise ValueError(
                "No existing friend was found matching id: {}".format(id))
        
    ```
    
    - Note that this function checks to see if there is a non-zero value
    for `cursor.rowcount`.  If not, it raises a `ValueError` exception.  
        
        - As a reminder, this type of exception is raised when a given parameter 
        is of the correct type, but a invalid value.
        
        - This will occur in this function when the value of the `id` parameter
        is set to something that has no match in the datastore, and therefore
        can not be deleted.
        
| [Next Exercise](exercise-11.md)
    