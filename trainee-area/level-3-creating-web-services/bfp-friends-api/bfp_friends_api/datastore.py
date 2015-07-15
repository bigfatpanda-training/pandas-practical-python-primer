"""
This modules provides functions to interact with our SQLite datastore.
"""

import sqlite3


def get_friends(ds_connection: sqlite3.Connection) -> dict:
    """
    Return a representation of all rows in the friends table.

    Args:
        ds_connection (sqllite3.Connection): An active connection to a
            sqllite datastore containing a friends table.

    Returns
        A JSON ready dictionary representing all rows of the friends table.
    """
    cursor = ds_connection.execute(
        'select id, first_name, last_name, telephone, email, notes '
        'from friends')

    friends_collection = list()
    for friend_row in cursor.fetchall():
        friends_collection.append(
            {"id": friend_row[0],
             "first_name": friend_row[1],
             "last_name": friend_row[2],
             "telephone": friend_row[3],
             "email": friend_row[4],
             "notes": friend_row[5]})

    return friends_collection


def get_friend(ds_connection: sqlite3.Connection, id: str) -> dict:
    """
    Obtain a specific friend record and return a representation of it.

    Args:
        ds_connection (sqllite3.Connection): An active connection to a
            sqllite datastore containing a friends table.
        id (str): An `id` value which will be used to find a specific
            datastore row.

    Returns
        A JSON ready dictionary representing a specific
        row of the friends table.
    """
    cursor = ds_connection.execute(
        'select id, first_name, last_name, telephone, email, notes '
        'from friends where lower(id) = ?',
        [id.lower()])

    friend_row = cursor.fetchone()

    if friend_row:
        return {
            "id": friend_row[0],
            "first_name": friend_row[1],
            "last_name": friend_row[2],
            "telephone": friend_row[3],
            "email": friend_row[4],
            "notes": friend_row[5]}


def add_friend(ds_connection: sqlite3.Connection, entry_data: dict):
    """
    Create a new row in the friends table.

    Args:
        ds_connection (sqllite3.Connection): An active connection to a
            sqllite datastore containing a friends table.
        entry_data (dict): The data needed to created a new entry.
    """
    ds_connection.execute(
        "insert into friends (id, first_name, last_name, telephone, email, notes) "
        "values (?, ?, ?, ?, ?, ?)",
        [entry_data['id'],
         entry_data['firstName'],
         entry_data['lastName'],
         entry_data['telephone'],
         entry_data['email'],
         entry_data['notes']])
    ds_connection.commit()


def fully_update_friend(ds_connection: sqlite3.Connection, entry_data: dict):
    """
    Update all aspects of given row in the friends table.

    Args:
        ds_connection (sqllite3.Connection): An active connection to a
            sqllite datastore containing a friends table.
        entry_data (dict): The data needed to update a given entry.  The
            `id` value of this dictionary is used to identify the entry
            to update.
    """
    ds_connection.execute(
        "UPDATE friends "
        "SET id=?, first_name=?, last_name=?, telephone=?, email=?, notes=? "
        "WHERE lower(id) = ?",
        [entry_data['id'],
         entry_data['firstName'],
         entry_data['lastName'],
         entry_data['telephone'],
         entry_data['email'],
         entry_data['notes'],
         entry_data['id'].lower()])
    ds_connection.commit()


def delete_friend(ds_connection: sqlite3.Connection, id: str) -> dict:
    """
    Delete a given entry from the friends table in a given SQLite connection.

    Args:
        ds_connection (sqllite3.Connection): An active connection to a
            sqllite datastore containing a friends table.
        id (str): An `id` value which will be used to find a specific
            datastore row to delete.
    """
    cursor = ds_connection.execute(
        'DELETE  '
        'from friends where lower(id) = ?',
        [id.lower()])

    if not cursor.rowcount:
        raise ValueError()

    ds_connection.commit()