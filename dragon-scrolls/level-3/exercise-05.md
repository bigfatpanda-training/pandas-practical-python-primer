[Previous](exercise-04.md) |  [Next](exercise-06.md)
## Exercise 5: Implement More `GET` Functionality 
[Code Files](../../training/level-3-interacting-with-web-services/bfp-reference/exercise_04)

In this exercise we will add some additional functions to our program that
retrieve additional information from the Github API.  We will pull back
information on users, repos, and even issues.

### There Is No Secret Ingredient: Github User Data
You may recall that in the results of `github_entry_point` there was an 
entry in the JSON that looked like this: `'user_url': 'https://api.github.com/users/{user}'`.

Github is awesome for providing URLs in their responses because it allows
others to write a program that can transverse the API by following URLs from 
request to request.  Placing links like this in an API is referred to 
these days as using **hypermedia**.  We'll do a little bit of that here,
but we will also cheat some in other examples to keep our code short.

Anyway, let's use that bit of data in our second function:

 
```python
def github_user_info(username: str) -> requests.Response:
    """
    Obtain information about a given user in Github.

    Args
        username: A str specifying a valid Github username.

    Returns
        A requests.Response object.
    """
    github_api_info = github_entry_point().json()
    url = github_api_info['user_url'].format(user=username)
    response = requests.get(url)
    return response

```
- Notice that we make use of our first function inside of our second function.
In particular, we extract the `user_url` key value from the dictionary
returned by `github_entry_point().json()`.

- Since the value of `github_api_info['user_url']` is 
`https://api.github.com/users/{user}` we can use the `str.format` method
to insert a new value where `{user}` appears in the string. And this is exactly
what we do, inserting the `username` function parameter.
 
- The final two lines of the function are the same as the first one.

- Execute this function, either in the `if __name__ == '__main__'` part of 
your script or from the command line.  Pass it `bigfatpanda-training` as the
username.  Inspect the JSON payload of the response and you should get 
something like this:

    ```python
    {'avatar_url': 'https://avatars.githubusercontent.com/u/12503354?v=3',
     'bio': 'Resources for Dragon Warriors in Training',
     'blog': None,
     'company': None,
     'created_at': '2015-05-18T21:59:35Z',
     'email': None,
     'events_url': 'https://api.github.com/users/bigfatpanda-training/events{/privacy}',
     'followers': 0,
     'followers_url': 'https://api.github.com/users/bigfatpanda-training/followers',
     'following': 0,
     'following_url': 'https://api.github.com/users/bigfatpanda-training/following{/other_user}',
     'gists_url': 'https://api.github.com/users/bigfatpanda-training/gists{/gist_id}',
     'gravatar_id': '',
     'hireable': None,
     'html_url': 'https://github.com/bigfatpanda-training',
     'id': 12503354,
     'location': None,
     'login': 'bigfatpanda-training',
     'name': None,
     'organizations_url': 'https://api.github.com/users/bigfatpanda-training/orgs',
     'public_gists': 0,
     'public_repos': 1,
     'received_events_url': 'https://api.github.com/users/bigfatpanda-training/received_events',
     'repos_url': 'https://api.github.com/users/bigfatpanda-training/repos',
     'site_admin': False,
     'starred_url': 'https://api.github.com/users/bigfatpanda-training/starred{/owner}{/repo}',
     'subscriptions_url': 'https://api.github.com/users/bigfatpanda-training/subscriptions',
     'type': 'Organization',
     'updated_at': '2015-05-20T17:19:55Z',
     'url': 'https://api.github.com/users/bigfatpanda-training'}
    ```


### There Is No Secret Ingredient: Github Repo Data
Still need to write.  See exercise-05 code files.

### There Is No Secret Ingredient: Github Repo Issues Data
Still need to write.  See exercise-05 code files.
    

| [Next Exercise](exercise-06.md)