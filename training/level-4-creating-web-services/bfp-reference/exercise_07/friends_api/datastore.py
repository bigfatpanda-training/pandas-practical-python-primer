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
    required_elements = friends[0].keys()
    if data is None:
        raise ValueError("You cannot create a friend without data.")
    elif not set(data).issuperset(required_elements):
        raise ValueError("Some of the data required to create a friend "
                         "was not present.  The following elements "
                         "must be present to create a friend: {}".format(
            required_elements))