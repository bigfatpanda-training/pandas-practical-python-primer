# Intro to CLIs
A CLI, or **command line interface**, is a program that exposes 
its functionality via the command-line.  I know, what a shock.

We've already been using a very sophisticated CLI - Vagrant.  Today, 
we are going to create our very own CLI that copies files using only 
the Python Standard Library.

## Goal 1: Create an ArgumentParser class
1. Create our module and add a docstring to it
2. Import the argparse module/library?
3. How do we learn stuff about the module?  
    * help()
    * [Official Documentation](https://docs.python.org/3/)
    
4. Create an instance of the `argparse.ArgumentParser` class.
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
    
## Goal 3: The result of `parser.parse_args()` => About `str` and `list` types
1. In Python, both of these object types are considered 
[sequences](https://docs.python.org/3.4/library/stdtypes.html#sequence-types-list-tuple-range) 
which means that a shared set of functionality are available
for all objects of their types.
2. Let's experiment with some of these methods.
 
## Goal 4: Organizational Pitstop
* Pythonic way of indicating that a script is callable as a program. 
`if __name__ == "__main__"` construct.  What does this get you?
* Break things into smaller chuncks with functions.
    * Create a function that parses command line input and returns the result.
    * Create a function stub that will be used to copy the files.

    


    


