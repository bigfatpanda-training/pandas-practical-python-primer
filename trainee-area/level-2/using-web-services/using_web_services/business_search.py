"""
This module interacts with a public Web API that provides business
listings.

The API docs are hosted at: http://api.searchcompany.us
"""

import requests

COMPANY_SEARCH_URL = "http://api.searchcompany.us/1.0/search"
COMPANY_RETRIEVAL_URL = "http://api.searchcompany.us/1.0/company"


def company_search(name: str):
    search_url = "{}/{}".format(COMPANY_SEARCH_URL, name)
    return requests.get(search_url)


def company_lookup(id: int):
    pass


if __name__ == "__main__":
    search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
    results = requests.get(search_url)

    company_ids = []   # Alternatively, company_ids = list()
    for company_record in results.json()['company']:
        company_ids.append(company_record['id'])

    # As List Comprehension
    # company_ids = [company_record['id'] for company_record in results.json()['company']]

    company_info = []
    for company_id in company_ids:
        lookup_url = "{}/{}".format("http://api.searchcompany.us/1.0/company", company_id)
        lookup_results = requests.get(lookup_url)
        company_info.append(lookup_results.json())

    # As List Comprehension
    # company_info = [
    #     requests.get("{}/{}".format(
    #         "http://api.searchcompany.us/1.0/company", company_id)).json()
    #     for company_id in company_ids]

    print(company_info)