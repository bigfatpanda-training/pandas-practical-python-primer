friends = [
    {
        "id": "BFP",
        "first_name": "Big Fat",
        "last_name": "Panda",
        "telephone": "574-213-0726",
        "email": "mike@eikonomega.com",
        "notes": "My bestest friend in all the world."
    },
    {
        "id": "VinDi",
        "first_name": "Vin",
        "last_name": "Diesel",
        "telephone": "I-HIT-PEOPLE",
        "email": "vdiesel4@supercool.edu",
        "notes": "Really annoying guy.  Will never amount to anything."
    }
]


def existing_friend(id: str) -> dict:
    """

    Args:
        id:

    Returns:

    """
    for friend in friends:
        if str(id).lower() == str(friend["id"]).lower():
            return friend
