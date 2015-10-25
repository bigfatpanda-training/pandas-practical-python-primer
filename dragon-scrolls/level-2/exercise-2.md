[Previous](exercise-1.md) |  [Next](exercise-3.md)
## Exercise 2: Create an ArgumentParser Object
Alright Dragon Warrior - let's review:

1. What type of object is a factory (or object generator) that creates other 
objects based on an internal pattern?
1. After a object is created, what function can you use to tell which 
factory object created it?

### There Is No Secret Ingredient
1. Create an instance of the `argparse.ArgumentParser` class and assign it a
name.
5. What are the options that we can pass to the constructor?
    * description
    * epilog
6. Add the call to `parse_args()` so that class can see it start to work.
    
## Goal 2: Add functionality to our Argument Parser
1. Remember that `argparse.ArgumentParser` is a class.  Classes have 
methods, which are like functions except that the share a namespace and
state.
2. How could we see what methods this class has? 
    * Online documentation or help()
3. Add an argument to the class which accepts a variable number of 
filesnames to copy.
    * `parser.add_argument(dest='filenames', metavar='filename', nargs='+', help="All the files to copy.")`
    * What do the options mean?

4. Add an additional argument to specify the destination of the copied files.
    * `parser.add_argument('-d', '--destination', required=True, dest='destination', help='Location to copy files to.')`
    
5. **Students:**  Add an additional optional argument to the parser.
    
## Goal 3: The result of `parser.parse_args()` => About `str` and `list` types
1. In Python, both of these object types are considered 
[sequences](https://docs.python.org/3.4/library/stdtypes.html#sequence-types-list-tuple-range) 
which means that a shared set of functionality are available
for all objects of their types.
2. Let's experiment with some of these methods.
 
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

## Interlude: Python 2 -> Python 3
1. Rebuilding the Vagrant machine to use the latest Vagrantfile.
    * `Vagrant destroy`
    * `Vagrant up`
2. Reconnecting PyCharm with the VM.
3. What does this get us right now? [Function Annotations](https://www.python.org/dev/peps/pep-3107/)
    
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

    


    


