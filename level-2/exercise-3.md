[Previous](exercise-2.md) |  [Next](exercise-4.md)
### Step 3: Get Information on a Specific Business 
* Refer to the online [API documentation](http://api.searchcompany.us) to see 
how to use the results of the search to get the information you need to get 
more information on a specific business.

* Pull out the necessary information from the JSON body/payload of the search
request.  Talk about what is happening here.

```python
if __name__ == "__main__":
    search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search/", "Panda")
    results = requests.get(search_url)
    
    company_ids = []   # Alternatively, company_ids = list()
    for company_record in results.json()['company']:
        company_ids.append(company_record['id'])
```
* Run the program interactively (`python -i [program_name]`) and use the 
`dir()` method on the `results` object and inspect the results of your 
`requests.get()` call.
    * Review: What is the difference between an _object method_ and an _object attribute_?
    * What happens if you try to invoke an attribute as a callable?
    * What happens if you try to invoke a method without callable syntax?
    
* Using the pprint module to print out the results of `results.json()` in an
understandable way.
    * Alternatively, run the program with `ipython` and you won't have to 
    import the `pprint` module as it does this under the covers for you.