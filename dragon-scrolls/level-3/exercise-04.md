[Previous](exercise-03.md) |  [Next](exercise-05.md)
## Exercise 4: Let's `GET` to it.
[Code Files](../../training/level-3-interacting-with-web-services/bfp-reference/exercise_03)

It's time to start interacting with your first API in Python. **Awesome!**

### There Is No Secret Ingredient: `requests.get`
Add the following to `github_api.py`:
 
```python
def github_entry_point() -> requests.Response:
    """
    HTTP GET `https://api.github.com`

    Obtain information about the Github API from its entry point.
    """
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

- Like all objects, they have various attributes and methods which you can
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
    >>> python -i github_api.py
    >>> import pprint
    >>> print(github_info.status_code)
    200
    ```
    - The status code of the HTTP response was 200, which means that there
    were no errors in processing the request.

- Now print out the HTTP headers that were included in the Response object:
`pprint.pprint(dict(github_info.headers))`:
    
    ```python
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
     ```
     
     > ![Extra Info](../images/reminder.png) Notice that we are converting
     `github_info.headers` into a `dict` before printing it?  This is because
      `github_info.headers` is a custom object that doesn't support 
      pretty-printing.  We have to convert it to an object that does so that
      `pprint` will work.
      
- Finally, let's take a look at the the actual payload/body of the `Response`
object by using `pprint.pprint(github_info.json())`:
 
     ```python
     {'authorizations_url': 'https://api.github.com/authorizations',
     'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}',
     'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}',
     'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}',
     'current_user_url': 'https://api.github.com/user',
     'emails_url': 'https://api.github.com/user/emails',
     'emojis_url': 'https://api.github.com/emojis',
     'events_url': 'https://api.github.com/events',
     'feeds_url': 'https://api.github.com/feeds',
     'followers_url': 'https://api.github.com/user/followers',
     'following_url': 'https://api.github.com/user/following{/target}',
     'gists_url': 'https://api.github.com/gists{/gist_id}',
     'hub_url': 'https://api.github.com/hub',
     'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}',
     'issues_url': 'https://api.github.com/issues',
     'keys_url': 'https://api.github.com/user/keys',
     'notifications_url': 'https://api.github.com/notifications',
     'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}',
     'organization_url': 'https://api.github.com/orgs/{org}',
     'public_gists_url': 'https://api.github.com/gists/public',
     'rate_limit_url': 'https://api.github.com/rate_limit',
     'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}',
     'repository_url': 'https://api.github.com/repos/{owner}/{repo}',
     'starred_gists_url': 'https://api.github.com/gists/starred',
     'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}',
     'team_url': 'https://api.github.com/teams',
     'user_organizations_url': 'https://api.github.com/user/orgs',
     'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}',
     'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}',
     'user_url': 'https://api.github.com/users/{user}'}
     ```

    - Notice that the JSON of the payload is represented as a Python dictionary.  
    This works out extremely well since the syntax of these two data structures
    are virtually identical.
    - As to the content itself, you can see that the base URL of the Github API
    provides a whole list of links that we can follow as we continue to develop 
    our program.  Let's do that, shall we?
    
> ![Example Code File Info](../images/information.png) For your convenience,
the example code files for this exercise include the various `print` 
statements that we did interactively so that you can reference them as a
whole later on.

| [Next Exercise](exercise-05.md)