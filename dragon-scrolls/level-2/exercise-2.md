[Previous](exercise-1.md) |  [Next](exercise-3.md)
## Exercise 2: Create an ArgumentParser Object
Alright Dragon Warrior - let's review:

1. What type of object is a factory (or object generator) that creates other 
objects based on an internal pattern?
1. After a object is created, what function can you use to tell which 
factory object created it?

In this exercise, we're going to use the `argparse` module to create an object
which knows how to parse command line arguments for use inside of your CLI.

### There Is No Secret Ingredient
1. Create an instance of the `argparse.ArgumentParser` class and assign it a
name.     
1. Add a call to `parse_args()` so that class can see it start to work.
1. Run your program with a `-h` option at the end.  What do you get?
1. Let's see what sort of things we can change about our object when we
are creating it.
     - Determine what some of the options that we can pass to the constructor? 
    What are the various ways to do this?  I can think of at least 3.
    - Choose 2-3 of the easy ones and add them.
    - Rerun your program with the `-h` option and see what has changes. 
    



    


