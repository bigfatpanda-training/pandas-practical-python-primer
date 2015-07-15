"""
This module interacts with a public Web API that provides business
listings.

The API docs are hosted at: http://api.searchcompany.us
"""

import requests

COMPANY_SEARCH_URL = "http://api.searchcompany.us/1.0/search"
COMPANY_RETRIEVAL_URL = "http://api.searchcompany.us/1.0/company"


def company_search(name: str) -> list:
    search_url = "{}/{}".format(COMPANY_SEARCH_URL, name)
    return requests.get(search_url).json()['company']   # Method Chaining

    # Without Method Chaining
    # results = requests.get(search_url)
    # json_payload = results.json()
    # company_records = json_payload['company']
    # return company_records


def companies_info(companies: list):
    # Use list comprehension because its pretty simple.
    company_ids = [company['id'] for company in companies]

    # Alternatively w/o list comprehension
    # company_ids = []   # Alternatively, company_ids = list()
    # for company in companies:
    #     company_ids.append(company['id'])

    # Don't use list comprehension because it isn't so simple.
    full_company_listings = []
    for company_id in company_ids:
        lookup_url = "{}/{}".format(COMPANY_RETRIEVAL_URL, company_id)
        lookup_results = requests.get(lookup_url)
        full_company_listings.append(lookup_results.json())

    return full_company_listings


if __name__ == "__main__":
    companies = company_search(name="Panda")
    information_on_companies = companies_info(companies=companies)
    print(information_on_companies)
