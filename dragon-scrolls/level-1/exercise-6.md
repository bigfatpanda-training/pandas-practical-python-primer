[Previous](exercise-5.md) |  [Next](exercise-7.md)
## Exercise 6: Mutable Sequence Types: Lists and Byte Arrays
Mutable sequences can be changed after they are created:
- Elements can be added, removed and replaced.  
- Element order can also be changed.
 
The Python docs indicate that the `list` and `bytearray` types are the 
common mutable sequences.  For our class, we'll only be using lists.

However, both types support all the [mutable sequence operations](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types).
 
### [Lists](https://docs.python.org/3/library/stdtypes.html#lists)
Extremely flexible and usable data structures.  We've already used them
numerous times.
- Represented internally as `list`.
- Holds any type of object.
- Uses more memory and is less efficient than equivalent tuples.
- We've already used lists a number of times in class so we won't go over
the common methods again here to add, remove, and reorder list elements.
- We have not yet demonstrated how we can replace a given element.  It's 
very easy.  You specify the element index (just like if you wanted to 
retrieve the value) and then use an assignment operator.

    ```python
    >>> example = [1, 2, 3, 4, 5]
    >>> example[0] = 11
    >>> example
    [11, 2, 3, 4, 5]
    ```
    
    > ![Question](../images/question.png) Now, look at the next item and
    ask yourself, *"What isn't Panda telling me? What else could I do?"*
- You can also delete elements by index number (or slice notation) like so:
    
    ```python
    >>> example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> del example[0]
    >>> example
    [2, 3, 4, 5]
    
    >>> example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> del example[0:5]
    >>> example
    [6, 7, 8, 9, 10]
    
    >>> example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> del example[0:5:2]
    >>> example
    [2, 4, 6, 7, 8, 9, 10]
    ```

### There Is No Secret Ingredient
#### Time/Space Efficiency Comparison of Tuples/Lists
I've said that tuples are more efficient than lists - both in storage size
and inspection/iteration.  Let's go ahead and prove that.

To do this, you would need to have some additional knowledge of things that 
we haven't covered yet.  So, **let's cheat!** Open the `exercise_6.py` file
in the `training/level-1/bfp-reference` folder.
 
Here's an overview of what's going on:

1. Use the `import` command to import the `sys` and `timeit` modules.

    > ![Info](../images/information.png) These modules/packages are part of
    > the **Python Standard Library**. You don't have to do anything to install
    > them.  We'll learn more about how `import` works at a later time.
    >
    > ![Question](../images/question.png) Where should the `import` statement
    > go in your file?  Remember PEP8!
    
1. Create a tuple and a list that each hold the numbers 0 to 500000 in them.
1. Use the `sys.getsizeof()` function to get the memory used by each of these
objects.  Which one is takes up more space?
1. Use the `timeit` module to see how long it takes iterate(loop) over each of
our test objects.
1. Run the file and see the results!


