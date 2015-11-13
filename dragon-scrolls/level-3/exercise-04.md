[Previous](exercise-02.md) |  [Next](exercise-04.md)
## Exercise 4: Let's `GET` to it.
[Code Files](../../training/level-3-interacting-with-web-services/bfp-reference/exercise_03)

It's time to start interacting with your first API in Python. **Awesome!**

### There Is No Secret Ingredient: `requests.get`
Add the following to `github_api.py`:
 
```python
def github_entry_point():
    url = "https://api.github.com"
    response = requests.get(url)
    return response


if __name__ == "__main__":
    github_info = github_entry_point()
```
- GitHub has one of the best, most standards compliant RESTful web services
out there.  One of the nice things about it is that you can learn a fair 
amount of how to use it without having to consult documentation.  
    - This has it limits, but its a lot more than most APIs out there.

- To find out the broad strokes of what functionality is available, we simply
issue a HTTP `GET` request the base url of the API: `https://api.github.com`.

- You'll see here that we are doing this by passing that url to `requests.get`.
    - The requests library provides a function corresponding to each of the
    HTTP methods.  So, you'll find there is `requests.post`, `requests.put`,
    `requests.patch`, and `requests.delete`.  
    - We will use these as we progess in this training level.
    
### There Is No Secret Ingredient: `Response` objects
    
- Calls to `requests.get` (or `requests.post`, etc) return a [`Response`](http://docs.python-requests.org/en/latest/api/#requests.Response) 
object representing the HTTP Response received from the server.

- Like all objects, the have various attributes and methods which you can
read about in the [online docs](http://docs.python-requests.org/en/latest/api/#requests.Response).

- Most commonly, we will be interested in the following:
    - `Response.status_code`: The HTTP status code of the response.
    - `Response.headers`: A dictionary-like object of the response headers.
    - `Response.json()`: A method which returns a dictionary of the parsed JSON
    content of the HTTP response body.  
        - This only works if the response body was in JSON, which will usually
        the case.  
        - Use `Response.content` for non-JSON payloads.
        
- Drop to the command line and run your program interactively so that we
can print these things out and see what they contain:
    ```python
    >>> python -i github.api
    >>> import pprint
    >>> print(github_info.status_code)
    200
    ```
    - The status code of the HTTP response was 200, which means that there
    were no errors in processing the request.
    
    >>> pprint.pprint(dict(github_info.headers))
    {'Access-Control-Allow-Credentials': 'true',
     'Access-Control-Allow-Origin': '*',
     'Access-Control-Expose-Headers': 'ETag, Link, X-GitHub-OTP, '
                                      'X-RateLimit-Limit, X-RateLimit-Remaining, '
                                      'X-RateLimit-Reset, X-OAuth-Scopes, '
                                      'X-Accepted-OAuth-Scopes, X-Poll-Interval',
     'Cache-Control': 'public, max-age=60, s-maxage=60',
     'Content-Encoding': 'gzip',
     'Content-Security-Policy': "default-src 'none'",
     'Content-Type': 'application/json; charset=utf-8',
     'Date': 'Fri, 13 Nov 2015 14:38:03 GMT',
     'ETag': 'W/"d251d84fc3f78921c16c7f9c99d74eae"',
     'Server': 'GitHub.com',
     'Status': '200 OK',
     'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload',
     'Transfer-Encoding': 'chunked',
     'Vary': 'Accept, Accept-Encoding',
     'X-Content-Type-Options': 'nosniff',
     'X-Frame-Options': 'deny',
     'X-GitHub-Media-Type': 'github.v3',
     'X-GitHub-Request-Id': '68B7E31C:7FBD:DEDF7A2:5645F5CB',
     'X-RateLimit-Limit': '60',
     'X-RateLimit-Remaining': '52',
     'X-RateLimit-Reset': '1447428654',
     'X-Served-By': 'bae57931a6fe678a3dffe9be8e7819c8',
     'X-XSS-Protection': '1; mode=block'}
    
    if __name__ == "__main__":
        import pprint
        github_info = github_entry_point()
        print(github_info.status_code)
        pprint.pprint(dict(github_info.headers))
        pprint.pprint(github_info.json())
    ```
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

### There Is No Secret Ingredient
    
| [Next Exercise](exercise-05.md)