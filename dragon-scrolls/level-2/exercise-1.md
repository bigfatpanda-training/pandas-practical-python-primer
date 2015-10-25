[Previous](readme.md) |  [Next](exercise-2.md)
## Exercise 1: Getting Started
Today is a great day! It's time to put together the knowledge of the basics
that you learned in level-1 to use.

Before we get started, let's touch on a couple of topics: docstrings and
the `import` statement.

### What's a Docstring Again?
Docstrings are special comments that you add to various objects - packages,
modules, functions, classes, and methods in particular that are parsed by
IDEs, help(), documentation generators, and other tools to provide information
to others about your code.  

Not having quality docstrings is signal (like not
following PEP8) to other Pythonistas that you don't really care about what
you're doing.  

Some highlights for now:
- All docstrings start and end with triple double quotes: 
    
    ```python
    """An example docstring."""
    ```
- Docstrings should be the first statement of whatever object is being
documented. In other words, they come before everything else.
- There are two flavors:
    - Single line: Used when the meaning of a given object is nearly obvious
    and straightforward.  These, by definition, must be short:
        
        ```python
        def big_number():
            """Return a big number."""
        ```
    - Multi-line: In practice, used the majority of the time.  These type of
    docstrings have a summary line and then a longer description with a line
    break in between:
    
        ```python
        def big_number(minimum=None, exponent=None):
            """
            Return a big number.
             
            This function returns a randomized big number.  The caller 
            is able to constrain the possible return values through
            two parameters.
            """
        ```
- Like PEP8, you should regularly review Python's docstring conventions, 
encoded in [PEP257](https://www.python.org/dev/peps/pep-0257/) until 
you know it by heart.

### Yeah! `import` Like a Rock Star!
The use of the `import` statement is universal outside of the most trivial
Python programs.  It is generally easy to use, but really quite complicated 
once you try to understand it.

For our purposes, here are the crucial bits to understand:
- The `import` statement loads the contents of another module (or package) and
assigns a name to it in the local the local scope/namespace.  In other words, 
it gives you access to code located in other files.

- When Python first encounters a call to `import`, it looks for the requested
module in the following order:
    1. Previously loaded modules: `sys.modules`
    1. Modules and packages of the Standard Library.
    1. Locations generally used for local code (stuff you develop) and 3rd
    party modules/packages that you've installed.  Generally, you can 
    


### There Is No Secret Ingredient
1. Create a module in the `dragon-warrior` folder for this level called:
`[your_github_username]_stdlib_cli.py`.  
   
    > ![Review](../images/reminder.png) What's the difference between a 
    **module** and a **package**?
1. Add a docstring to your module.  It doesn't matter too much right now
what it says.  Perhaps start with this: `This module provides a CLI that...`
1. Import the `argparse` module.
    
    > ![Review](../images/reminder.png) The `argparse` module is part of
    the Python Standard Library.  According to PEP8, where should it's 
    import statement go?