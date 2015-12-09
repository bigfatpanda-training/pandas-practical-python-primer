friends = [
    {
        "id": "BFP",
        "first_name": "Big",
        "last_name": "Panda",
        "telephone": "574-213-0726",
        "email": "mike@eikonomega.com",
        "notes": "My worst instructor ever."
    },
    {
        "id": "VinDi",
        "first_name": "Vin",
        "last_name": "Diesel",
        "telephone": "I-HIT-PEOPLE",
        "email": "vdiesel@hollywood.com",
        "notes": "Zzzzzzzzzz."
    }
]

def existing_friend(id: str) -> dict:
    """
    Return a representation of friend resource that matches a given
    Args:
        id:

    Returns:

    """

    for friend in friends:
        if id.lower() == friend['id'].lower():
            return friend