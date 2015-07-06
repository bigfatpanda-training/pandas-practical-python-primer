[Previous](exercise-2.md) |  [Next](exercise-4.md)
## Add HTTP GET Support to our Web Service API
The first thing that we are going to do is add support for HTTP GET operations
to our API.  We will add this for both the **resource collection** and 
**individual resource** levels.

> ![Question](../images/reminder.png) What is the difference between those two terms?

#### Step 1: Add a function that will return information on all our friends

```python

```

* Refer to the online [API documentation](http://api.searchcompany.us) to see 
how to use the results of the search to get the information you need to get 
more information on a specific business.

* Pull out the necessary information from the JSON body/payload of the search
request.  Talk about what is happening here with the class.

    ```python
    if __name__ == "__main__":
        search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
        results = requests.get(search_url)
        
        company_ids = []   # Alternatively, company_ids = list()
        for company_record in results.json()['company']:
            company_ids.append(company_record['id'])
    ```

* **Advanced Tidbit**: Pythonistas use a feature call _list comprehensions_ to 
dynamically generate lists like the one we've made without the need to
define the list ahead of time and construct a loop.  Here's how that would look:

    ```python
    if __name__ == "__main__":
        search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
        results = requests.get(search_url)
        
        # List Comprehension (Cool points in Python bars)
        company_ids = [company_record['id'] for company_record in results.json()['company']]
    ```

* Make additional calls to the API to retrieve detailed information on each 
business ID that you've obtained.

    ```python
    if __name__ == "__main__":
        search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
        results = requests.get(search_url)
        
        company_ids = []   # Alternatively, company_ids = list()
        for company_record in results.json()['company']:
            company_ids.append(company_record['id'])
            
        company_info = [] 
        for company_id in company_ids:
            lookup_url = "{}/{}".format("http://api.searchcompany.us/1.0/company", company_id)
            lookup_results = requests.get(lookup_url)
            company_info.append(lookup_results.json())
            
        print(company_info)
    ```
    
* What would this look like using a list comprehension? What about the Zen of Python?

    ```python
    if __name__ == "__main__":
        search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
        results = requests.get(search_url)
    
        company_ids = []   # Alternatively, company_ids = list()
        for company_record in results.json()['company']:
            company_ids.append(company_record['id'])
    
        company_info = [
            requests.get("{}/{}".format(
                "http://api.searchcompany.us/1.0/company", company_id)).json()
            for company_id in company_ids]
    
        print(company_info)
    ```
