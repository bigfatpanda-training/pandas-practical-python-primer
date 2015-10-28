[Previous](exercise-5.md) |  [Next](exercise-7.md)
## Exercise 6: Building a `copy_files` Function
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


## Goal 4: Organizational Pitstop
* Pythonic way of indicating that a script is callable as a program. 
`if __name__ == "__main__"` construct.  What does this get you?
* Break things into smaller chunks with functions.
    * Create a function that parses command line input and returns the result.
    * Create a function stub that will be used to copy the files.
    
## Goal 5: Introduction to Subprocess
The subprocess module allows us to make calls to other programs on your 
system, Python or otherwise.  We can then capture the output of these 
programs for evaluation.

1. import the `subprocess` module
2. Add content to the function stub that we created earlier to process
the program arguments and copy the files.
    * Use `help(subprocess.check_output)` or online documentation to see
    what this function does.
    * How to iterate over an object?
        * For loops, `iter()`, and `hasattr()`
3. How might we go about utilizing `subprocess.check_output` to actually 
copy files to a different location?
    * What are the necessary arguments?
    * What type of arguments does the underlying program (`cp`) take
    that might be useful to use?
4. How to we get the result of the `subprocess.checkout_output` operation?
5. How can we display the result to the user?
    * How can we get rid of the newline that appears to be printed?
    * Talk about method chaining: `str.method().method()`
    
## Goal 6: Adding Conditional Logic and Exception Handling
In this step we are going to add somethings into our program that *can* make
it explode depending on the input we receive from the user.  We'll look at
a couple of different ways of dealing with this added complexity.

1. Add an if/else statement to check for the existence of non-empty new_names 
function parameter value.
    * Options for checking if for non-empty : `if new_names vs. if new_names is not None`
        * Objects that evaluate to `False` in if statements:
            * None
            * False
            * zero for numeric types
            * Empty sequences (tuples, lists, strings, etc)
            * Empty dictionaries
    * What is going on with `new_filenames[files.index(file)])`?
    * Review `str.format()`
    * So what is going to happen if there aren't enough names in `new_names`
    to match the number of files in `files`?
    
2. Add Exception handling to deal with the IndexError that we've discovered!
    * Talk about error handling in Python: `try...except...else...finally`
    ```
    try:
        1/0
    except ZeroDivisionError:
        print("You did something illegal.")
    else:
        print("What you did was fine.")
    finally:
        print("You did something and it doesn't matter to me what it was.")
    ```
    * What goes in each section?
    * How much should go into the `try` block?
    * Add exception handling for the `IndexError` that will occur if we attempt
    to reference an index that doesn't exist in `new_filenames`.
    * Run the program using a variety of inputs trying to exercise the 
    different code paths.


## Goal 7: Becoming a multi-purpose CLI
We've made great progress thus far.  Now let's take the next (and final) step
in this training level and turn our CLI into something that can handle more
than one type of task.  Specifically, let's add the ability for our 
program to move files as well as copy them.

1. Add subparsers to your argparse.Argument parser object.  Talk about what
this is doing to the object.  
    ```
    subcommand_parsers = parser.add_subparsers(
            title="Available Commands",
            description="The following sub-commands are available.",
            dest="command")
    subcommand_parsers.required = True
    ```
    
    * Objects have attributes which are themselves objects.
    * What does `self._subparsers` mean?  `self` and "private" attributes.
    
2. Create two subparsers for the `move` and `copy` commands.
    ```
    copy_parser = subcommand_parsers.add_parser(name='copy', help="Copy Files")
    move_parser = subcommand_parsers.add_parser(name='move', help="Move Files")
    ```
    
    * Temporarily comment out the all of the `parser.add_argument` calls
    and see how the program now looks from the command line.
    
3. Add the `parser` arguments to both `move_parser` and `copy_parser`.
    * See how this affects the program operation.
    * Pay attention to how code is being repeated here.  This is a bad
    thing.  Violation of DRY.  We'll come back to it later if we have time.

     