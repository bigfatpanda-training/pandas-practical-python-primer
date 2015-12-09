friends = [
    {
        "id": "BFP",
        "firstName": "Big Fat",
        "lastName": "Panda",
        "telephone": "574-213-0726",
        "email": "mike@eikonomega.com",
        "notes": "My bestest friend in all the world."
    },
    {
        "id": "VinDi",
        "firstName": "Vin",
        "lastName": "Diesel",
        "telephone": "I-HIT-PEOPLE",
        "email": "vdiesel4@supercool.edu",
        "notes": "Really annoying guy.  Will never amount to anything."
    }
]


def create_friend(data: dict):
    """
    Create a new friend entry is our datastore of friends.

    Args:
        data: A dictionary of data for our new friend.  Must have
            the following elements: ['id', 'firstName', 'lastName',
            'telephone', 'email', 'notes']

    Raises:
        ValueError: If data is None, doesn't contain all required
            elements, or a duplicate id already exists in `friends`.
    """
    if data is None:
        raise ValueError(
            "`None` was received when a dict was expected during "
            "the attempt to create a new friend resource.")

    required_elements = set(friends[0].keys())
    if not required_elements.issubset(data):
        raise ValueError("Some of the data required to create a friend "
                         "was not present.  The following elements "
                         "must be present to create a friend: {}".format(
            required_elements))

    for element in data:
        if element not in required_elements:
            data.pop(element)

    for friend in friends:
        if data['id'].lower() == friend['id'].lower():
            raise ValueError("A friend already exists with the "
                             "`id` specified: {}".format(data['id']))

    friends.append(data)


def update_friend(id: str, data: dict):
    """
    Update an existing friend entry is our datastore of friends.

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

    #TODO: Remove extraneous data elements.

    for friend in friends:
        if id.lower() == friend['id'].lower():
            friend.update(data)
            return

    raise ValueError("No existing friend was found matching id: {}".format(id))


def destroy_friend(id: str):
    """
    Remove an existing friend entry from our datastore of friends.

    Args:
        id: The id value of the friend to delete.

    Returns:
        ValueError: If the `id` parameter doesn't match any existing
        friend entries in our datastore.

    """
    for friend in friends:
        if id.lower() == friend['id'].lower():
            friends.remove(friend)
            return

    raise ValueError("No existing friend was found matching id: {}".format(id))
