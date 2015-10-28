[Previous](exercise-3.md) |  [Next](exercise-5.md)
## Exercise 4: Some Design Choices with CLIs
In the last exercise, we specified that our first program argument `filenames`, 
would be a positional element that could one or more filenames as its value.  
Here's an example of doing that:
```python
import argparse

parser = argparse.ArgumentParser(
    prog="My Cool Program",
    description="My cool program does a lot of cool things.",
    epilog="Thanks for using my cool program")

parser.add_argument("filenames", nargs="+", metavar="FILENAME",
                    help="Names of files to copy.")
```

- Setting `nargs` to `+` makes the program accept a variable number of values,
but require at least one.
- The `metavar` and `help` parameters augment information that is presented
when a user invokes your program with the `-h` or `--help` flags. 
    - `metavar` allows you to override how the name of the parameter
    will appear in the help dialogue.
    - `help` allows you to specify additional information about the argument
    to the user..
    
Chances are the you created another positional argument to specify 
your destination argument:
```python
parser.add_argument('destination', help='Location to copy files to.')
```

If so, this works ok:
```python
>>> python stdlib_cli.py test_filename1 test_filename2 /path/to/my/destination
Namespace(destination='/path/to/my/destination', filenames=['test_filename1', 'test_filename2'])
```    
The `argparse` library was intelligent enough to pull the last value from
the command line and assign it to `destination` and let the rest of the values
be assigned to `filenames`.  

This approach has its limit though. It would not work if you want to have 
multiple positional arguments that accept more than one value.  For example,
if we changed if we defined the destination argument like so: 
```python
parser.add_argument('destinations', nargs='+', metavar='DESTINATION'
                    help='Location to copy files to.')
```

Then our program wouldn't be able to correctly decipher what values to belong 
to `filenames` and what belong to `destinations`:
```python
>>> python stdlib_cli.py test_filename1 test_filename2 /path/to/my/destination1 /path/to/my/destination2
Namespace(destination='/path/to/my/destination2', filenames=['test_filename1', 'test_filename2', '/path/to/my/destination1'])
```
- See how one of our destinations got lumped into `filenames`?
 
### An Alternative: Optional, or Keyword Command Line Arguments
Instead of using positional command line arguments, you use what the `argparse`
documentation refers to an "optional" arguments.

What is means by this is that these arguments are specified on the command line
by the using of flags.  The help option that is invoked with `-h` is a good 
example.

They can also take values and can appear in any order.  But the real neat
thing is that you can also make them required.  This effectively allows you
to have required keyword arguments for your programs, allowing your users
to specify them in whatever order they want.

To change a positional argument to an required keyword argument you have to:

1. Change the name (the first parameter in `add_argument`) into something that 
begins with either `-` or `--`.  
    
    > ![info](..images/information.png) You can actually specify both a short
    flag `-` and long flag `-` name.  Look in the docs for an example of this.
    
2. Pass `required=True` in your call to `add_argument`.
 
### There Is No Secret Ingredient
1. Update `filesnames` and `destination` positional arguments to be 
required keyword arguments.  `filesnames` should still take multiple values
while `destination` should take a single value.

1. When you've got it right, you should be able to specify the two arguments
on the command line in whichever order and get something like this for the 
output:
```python
>>> python stdlib_cli.py -d /example/location -f example_file1 example_file2
Namespace(destination='/example/location', filenames=['example_file1', 'example_file2'])
```

1. Do some edge case checking:
    - Does the program allow you to specify multiple files?
    - Does it error (as it should) if you try to give it multiple destinations?
    - Anything else you can think of to check?