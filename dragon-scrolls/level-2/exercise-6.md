[Previous](exercise-5.md) |  [Next](exercise-7.md)
## Exercise 6: Building a `copy_files` Function
In this exercise, we are going to build a function that will take
the arguments that we get from the command line and copy some
files from one location to another.

### There Is No Secret Ingredient: Create the Function
1. In `file_ops.py` Add a module docstring that says something like this:
    
    ```python
    """This modules provides various functions for operating on files."""
    ```
1. Create a function called `copy_files`:
    - Should take two parameters:
        - `files`: Which you should annotate as a list.
        - `destination`: Which should be annotated as a string.
        
1. Add a multi-line docstring for the function. We will use 
[Google's method](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments) for documenting the function arguments.

1. Create a `for` loop to iterate over each file in files.  For the
moment, just add a `pass` statement inside of the loop.

##### Snapshot of `file_ops.py`
Here a snapshot of what your `file_ops.py` module should look like
right now.  Now that our code files are getting longer, I'll provide
these from time to time.

```python
"""
This modules provides various functions for operating on files.
"""


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A str specifying the destination for copied
            files.
    """

    for file in files:
        pass
```

> ![Question](../images/question.png) Now that our function exists, what 
should be added to the module docstring according to PEP 257?

### Interlude: Introduction to Subprocess
The subprocess module allows us to make calls to other programs on your 
system, Python or otherwise.  We can also capture the output of the programs
that we call for evaluation.

We're going to use it to actually perform the copy operation and perhaps more
later.  Ok, definitely more.

### There Is No Secret Ingredient: Finishing `copy_files`
1. import the `subprocess` module. PEP8: Where does it go?
1. In the loop, add this:

    ```python
    for file in files:
        operation_result = subprocess.check_output(
            args=['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT)
    ```
    
    - About `subprocess.check_output` 
        - Executes a command one the system specified and returns the output.
        
        - The `args` list is used to construct the command to be executed. 
        Putting each item in a list allows Python to properly escape characters.
        Might want to double check that.
        - `stderr=subprocess.STDOUT` makes the function return normal and
        error output. Otherwise, error messages can be lost.
        
        - Check out `help(subprocess.check_output)` or the online docs for 
        alot more information on this function and what you can do with it.
    - In our case, we are executing the Linux `cp` command with a couple of
    flags, the file to copy, and the destination.
1. Add a call to `print` to output `operation_result` for each loop iteration.