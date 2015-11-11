[Previous](exercise-1.md) |  [Next](exercise-3.md)
### Step 2: Use the `requests` library to search for companies based on name 
* Use the `requests.get()` function to search for companies that have a given
string in their name.
```python
if __name__ == "__main__":
    search_url = "{}/{}".format("http://api.searchcompany.us/1.0/search", "Panda")
    results = requests.get(search_url)
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
