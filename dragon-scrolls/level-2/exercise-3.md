[Previous](exercise-2.md) |  [Next](exercise-4.md)
## Exercise 3: Add Arguments to your ArgumentParser
We've got an argument parser now.  Which is awesome, well, maybe not.
It doesn't actually parse anything yet.

Try call the program and passing it something other than `-h`. It won't turn
out so well.

Let's make it better by adding some argument definitions to our 
`ArgumentParser` object. To be more specific, let's add some 
argument definitions that would allow us to copy files from one
location to another.
    
### There Is No Secret Ingredient
1. Remember that `argparse.ArgumentParser` is an object with methods. Use the
`help` function to learn about the `ArgumentParser.add_argument` method.
    - Not very helpful is it.  Ok, let's go to the 
    [online docs](https://docs.python.org/3/library/argparse.html#the-add-argument-method).

1. Add a positional argument to the object which accepts a variable number of 
filenames to copy (but requires at least one).

1. Wrap the call to `parser.parse_args` with a `print` function.
1. Now run your program and pass it a copy of pretend files as arguments.
What gets printed out now?

1. Now add an additional argument definition specifying the location to
copy the file(s) to.  