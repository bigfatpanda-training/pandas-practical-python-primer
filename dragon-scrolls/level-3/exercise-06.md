[Previous](exercise-05.md) |  [Next](exercise-07.md)
## Exercise 6: Reimagining our Program with Classes 
[Code Files](../../training/level-3-interacting-with-web-services/bfp-reference/exercise_05)

Up to this point in our course, the highest level of code encapsulation has
been functions.  But our inefficient reuse of `github_entry_point` is like
the smell of rotten noodles.  It's a sign that there is a better way.

Classes allow us to group a related set of functionality that share access
to common data elements.  Using more familiar terms, a class allows a set
of methods to share common data attributes.

In our case, we want all our functions to have access to the results of 
`github_entry_point` without having to call it over and over again.

**Let's get started.**

### There Is No Secret Ingredient: The Github Class
At the top of your file, add the following:
```python
class Github:
    urls = requests.get("https://api.github.com").json()
    
    def __init__(self, oath_token: str):
        self.oauth_token = oauth_token
```
- Here's the beginning of our class.
  
- To define a class you have to use the `class` keyword followed by a name. 
Remember that PEP8 indicates that our class names should use UpperCamelCase 
syntax.

- The first line of the class definition (`urls = requests.get...`) creates
a **class attribute**.  This are data attributes that are shared between
all objects that are generated from this class.
    
    > ![Remember](../images/reminder.png) Remember that objects that come
    from a given class are also called **instances** of that class.
    
- The `__init__` method is a constructor.  When you generate a new object from
the class - `my_github_object = Github()` - this method is called to set
the initial state of the object.
    - You can see here that this method takes two parameters, `self` and 
    `oauth_token`.
    - All object methods take `self` as their first parameter.  If you want
    you can just take that as a fact on go on your merry way, making sure
    that is the first parameter of all your methods.  If you want your
    head to explode a little, read the next sidebar.
    
        > ![About `self`](..images/information.png) In a sense, the methods 
        > actually belong to the class, not the instances that spring
        > from the class.  So, when you call an object method, it actually 
        > ends up calling the method on the class.  The class needs to know
        > which instance is being affected by the method, and a reference
        > back to the instance is contained in the `self` parameter.
        
    - When you actually, call you methods, you don't specify a `self` 
    parameter.  Python inserts the appropriate value for you.
    
    - The `oauth_token` parameter is just like any other function/method 
    parameter.  Indicating a value that needs to be passed into the constructor.
    
    
### There Is No Secret Ingredient: Calling on Github Class (i.e. Object Factory)
Let's complete our little class here by adding an appropriate docstring to it
and then try creating a couple of instance objects from it.

```python
class Github:
    """
    Provides access to the Github API.

    Class Attributes:
        urls: Github API url templates for accessing various functionality.

    Attributes:
        oauth_token: A valid OAuth oauth_token for access the API.
    """
    urls = requests.get("https://api.github.com").json()

    def __init__(self, oauth_token: str):
        self.oauth_token = oauth_token
        

if __name__ == "__main__":
    github_1 = Github(oauth_token='pretend token 1')
    github_2 = Github(oauth_token='pretend token 2')
```

- Run your program interactively at the common line and see how each 
object will have a unique `oauth_token` but share the same value for
`urls`.

- What happens if you try to change the value of `urls`?  Does it change
on both objects?


| [Next Exercise](exercise-07.md)