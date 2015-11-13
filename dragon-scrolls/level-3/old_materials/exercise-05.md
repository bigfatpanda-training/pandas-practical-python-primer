[Previous](exercise-3.md) |  [Next](exercise-5.md)
### Step 4: Organize Program
* Let's take the URL's of the API and make them into _constants_.
    ```python
    ...
    import requests
    
    COMPANY_SEARCH_URL = "http://api.searchcompany.us/1.0/search"
    COMPANY_RETRIEVAL_URL = "http://api.searchcompany.us/1.0/company"
    
    if __name__ == "__main__":
        ...
    ```
    * Follow PEP8 naming conventions.  Why might this be important?
    * What is a constant? Why would we do this?
    * Why am I placing them outside of `if __name__ == "__main__"`
    
* Create a function that uses the search functionality of the API.
    
    ```python
    def company_search(name: str):
        search_url = "{}/{}".format(COMPANY_SEARCH_URL, name)
        return requests.get(search_url).json()['company']   # Method Chaining
    
        # Without Method Chaining
        # results = requests.get(search_url)
        # json_payload = results.json()
        # company_records = json_payload['company']
        # return company_records
    ```

* Create a function that uses the company lookup functionality of the API.

    ```python
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
    ```   

* Simplify the `if __name__ == "__main__"` code block:

    ```python
    if __name__ == "__main__":
        companies = company_search(name="Panda")
        information_on_companies = companies_info(companies=companies)
        print(information_on_companies)
    ```

