[Previous](exercise-3.md) |  [Next](exercise-5.md)
## Exercise 4: Sequence Types
There are many common types that belong to the Sequence family: 
strings, tuples, lists, and ranges. Additionally, there are the Bytes and
Byte Array types.

First, we'll cover what is common amongst all sequence types and then 
take a look at the specifics of each type.

### Definition
The Python documentation says that these types "represent finite ordered sets 
indexed by non-negative numbers."  Let's translate:
- Sequences are containers for other objects.
- They keep(or remember) the order of the objects that they contain.
- You can access the elements of a sequence via their non-negative index values.  
    
### Shared Functionality
All sequences share a core set of functionality.  That is what makes them
a sequence type!  

For demonstration purposes, let's assume that we have a list with the numbers
1-10 in it: `my_cool_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.  We'll use
that list to demonstrate common operations:

- You can access the sequence elements by their index position:
    ```python
    >>> my_cool_list[3]
    4
    ```
    
    > ![Information](../images/information.png) Here's a fun and often helpful
    > trick.  You can also use negative numbers to pull out elements by index
    > value.  **WAT?** Yup. It basically pulls them out in reverse order. 
    >    
    > ```python
    > >>> my_cool_list[-1]
    > 10
    > >>> my_cool_list[-3]
    > 8
    > ```
    >
    > The thing to remember is that since you can get negative 0, you have to
    > start with `-1` to get the last element of the sequence. `-2` gets the
    > second to last and so on.

- The `len()` function will return how many objects are held inside a sequence:
    ```python
    >>> len(my_cool_list)
    10
    ```
    
- The `min()` function will return the smallest element in a sequence if the
elements can be sorted:
    ```python
    >>> min(my_cool_list)
    1
    ```
    
- The `max()` function return the smallest element in a sequence:
    ```python
    >>> max(my_cool_list)
    10
    ```
        
- The `index` method will return the first occurrence of a given value in
the sequence:
    ```python
    >>> my_cool_list.index(10)
    9
    ```
    
    > ![Question](../images/question.png) What other parameters can be passed
    to the index method?  Do you remember how to find out?  It's in a previous
    exercise.
    
- The `count` method will return the number of times a given value exists
in the sequence:
    ```python
    >>> my_cool_list.index(5)
    1
    ```
    
- Sequences support **membership evalation**:
    - To see if an element exists in a sequence:
        ```python
        >>> 5 in my_cool_list
        True
        
        >>> "test string" in my_cool_list
        False
        ```
    
    - To see if an element doesn't exist in a sequence:
        ```python
        >>> 5 not in my_cool_list
        False
        
        >>> "test string" not in my_cool_list
        True
        ```
    
- Sequences support **slicing** syntax. 
    - This looks like accessing an element by index, and is really just 
    an extension of the same idea.
    - There are two flavors: `sequence[index1:index2]` and `sequence[index1:index2:step]`
        - The first flavor will return a new sequence - called a slice, of the
        elements of the original sequence that existed at from index1 up to 
        but not including index2.
        
            - So, if `my_cool_list = [1, 2, 3, 4, 5]` then `my_cool_list[1:3]` 
            would be `[2, 3]`.
            
        - The second flavor also returns a slice (or portion) of the original
        sequence in the same way as the first. However, the value of `step` 
        will further limit what is included in the slice.  It it used as an 
        specification to control how many elements to skip between each one
        chosen for inclusion.
            - I don't really like that explanation, so I really doubt you
            do either.  Let's look at it practically and it will make more
            sense.
            - Assume that `my_cool_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
            - `my_cool_list[0:6:1]` would come back with `[1, 2, 3, 4, 5, 6]`.
            This is same as `my_cool_list[0:6]`. 
            - Now let's change it `my_cool_list[0:6:2]`.  What do we get back?
            `[1, 3, 5]` You can see that it only returned every second element.
            Change it to three and it will only return every three element.
                                   
### There Is No Secret Ingredient
1. Create `my_cool_list` with some random numbers in it.
1. Access the various 1st and last elements of the list by their index position.
    1. What happens if you use an index number that doesn't exist?
    1. Don't forget to try negative index numbers.
2. Use `len()` to see how many elements are in it.
3. Use `min()` & `max()` and see what you get.
    1. Added some strings to th list and try `min()` and `max()` again.  
What happens?  What can you learn from that?
5. Use the `index` and `count` methods to see the index location and number
of times certain values exist in your list.
    1. What happens if you pass a nonexistent value to these methods?
1. Use the `in` and `not in` operators to test for the existence of values 
in your list.
1. Use the slicing syntax to get:
    1. The 2nd to 4th elements.
    2. The 5th to 10th elements, but skipping every other element.
    3. Can you figure out a way to get elements in reverse order using slice
    notation?

#### Further Reading
[Python Language Reference: Sequence Types](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)  
[Python Standard Library Docs: Sequence Types](https://docs.python.org/3.5/library/stdtypes.html#sequence-types-list-tuple-range)




