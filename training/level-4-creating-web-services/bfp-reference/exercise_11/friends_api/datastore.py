"""
This modules provides functions for creating, updating, and deleting
friend records from our database.
"""

import sqlite3


class Datastore:
    """
    Provides an interface to an SQLite database and associated methods.
    """

    def __init__(self):
        self.connection = sqlite3.connect("/tmp/friends.db")

    def friends(self) -> dict:
        """
        Return a representation of all rows in the friends table.

        Returns
            A JSON ready dictionary representing all rows of the friends table.
        """
        cursor = self.connection.execute(
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

        if self.friend(data['id']):
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
