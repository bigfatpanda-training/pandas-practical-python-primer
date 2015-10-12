[Previous](exercise-3.md) |  [Next](exercise-5.md)
## Exercise 4: Sequence Types
There are three common types that belong to the Sequence family: 
strings, tuples, and lists.

The Python documentation says that these types "represent finite ordered sets 
indexed by non-negative numbers."  Let's translate:
- Sequences are containers for other objects.
- They keep(or remember) the order of the objects that they contain.
- You can access the elements of a sequence via their non-negative index values.
You've seen this already: `my_cool_list[0]`
    - However, see what happens if you try to use a small negative number
    as the index value.  What happens?  What about a large negative index number?

Here are some other common characteristics of Sequence types:
- You can use the `len()` function to see how many objects are held 
inside the sequence.
- They support **slicing** syntax. 
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


Sequences are distinguished according to their mutability:

Immutable sequences
An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be changed; however, the collection of objects directly referenced by an immutable object cannot change.)

The following types are immutable sequences:

Strings
A string is a sequence of values that represent Unicode code points. All the code points in the range U+0000 - U+10FFFF can be represented in a string. Python doesn’t have a char type; instead, every code point in the string is represented as a string object with length 1. The built-in function ord() converts a code point from its string form to an integer in the range 0 - 10FFFF; chr() converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object. str.encode() can be used to convert a str to bytes using the given text encoding, and bytes.decode() can be used to achieve the opposite.

Tuples
The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). An empty tuple can be formed by an empty pair of parentheses.

Mutable sequences
Mutable sequences can be changed after they are created. The subscription and slicing notations can be used as the target of assignment and del (delete) statements.

There are currently two intrinsic mutable sequence types:

Lists
The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.)

The extension module array provides an additional example of a mutable sequence type, as does the collections module.    



