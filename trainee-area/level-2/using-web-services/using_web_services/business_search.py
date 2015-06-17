"""
This module interacts with a public Web API that provides business
listings.

The API docs are hosted at: http://api.searchcompany.us
"""

import requests

COMPANY_SEARCH_URL = "http://api.searchcompany.us/1.0/search/"
COMPANY_RETRIEVAL_URL = "http://api.searchcompany.us/1.0/company/"


def company_search(name: str):
    search_url = "{}/{}".format(COMPANY_SEARCH_URL, name)
    return requests.get(search_url)


def company_lookup(id: int):
    pass


if __name__ == "__main__":
    results = company_search("Indiana")