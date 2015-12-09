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
        ValueError: If data is None or doesn't contain all required
            elements.
    """
    if data is None:
        raise ValueError(
            "`None` was received when a dict was expected during "
            "the attempt to create a new friend resource.")

    required_elements = set(friends[0].keys())
    if not required_elements.issubset(data):
        raise ValueError("Some of the data required to create a friend "
                         "was not present.  The following required elements "
                         "must be present to create a friend: {}".format(
            required_elements))

    for friend in friends:
        if data['id'].lower() == friend['id'].lower():
            raise ValueError("A friend already exists with the "
                             "`id` specified: {}".format(data['id']))

    friends.append(data)



def existing_friend(id: str) -> dict:
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
