[Previous](exercise-4.md) |  [Next](exercise-6.md)
## Exercise 5: Let's Get Multi-Module In Here
Alright, it's time to do some awesome stuff!

Most programs stretch across multiple modules in a package structure.
It's time for yours to start doing that as well.

#### What's a Package Again?
A package in Python is a group of modules that share a common
directory structure.  All that you have to do change a normal 
directory into a package is to and an empty `__init__.py` file
in the directory.

If this exists, it will allow modules within the package to import
things from each other.

### There is No Secret Ingredient
1. Create a new directory `[your_github_username]` in the 
`level-2-command-line-interfaces/dragon-warrior` folder.  Then create
a new `__init__.py` file inside of it.  

    > ![Extra](../images/reminder.png) You can use the `New` -> 
    `Python Package` PyCharm command if you right-click on the `dragon-warrior`
     to perform both of these steps for you.  Just remember to delete the
     `__author__` metadata tag from the `__init__.py` file it creates.
1. Move your CLI program into it and rename it to `stdlib_cli.py`.
1. Create another Python module named `file_io.py` inside the package.
1. Here's what the folder structure should look like:
```bash
>>> ls [your_github_username]
file_io.py  __init__.py  stdlib_cli.py
```