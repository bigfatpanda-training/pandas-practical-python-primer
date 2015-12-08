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
    required_elements = set(friends[0].keys())
    try:
        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))
    except TypeError:
        raise ValueError("No data was received.") from TypeError

    for element in data:
        if element not in required_elements:
            data.pop(element)

    for friend in friends:
        if data['id'].lower() == friend['id'].lower():
            raise ValueError("A friend already exists with the "
                             "`id` specified: {}".format(data['id']))

    friends.append(data)