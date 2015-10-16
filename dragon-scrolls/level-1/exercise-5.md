[Previous](exercise-4.md) |  [Next](exercise-6.md)
## Exercise 5: Immutable Sequence Types: Strings, Tuples and Ranges
The members of [Immutable](https://www.google.com/?gws_rd=ssl#q=immutable) 
sequence types cannot be changed once created.  The three common ones that
we will consider here are strings, tuples, and ranges.

### [Tuples](https://docs.python.org/3.5/library/stdtypes.html#tuples)
- Represented internally as `tuple`
- You can put anything inside of a tuple.  It's a simple container.
- The objects that you put into the tuple can be of mixed type.
- You don't have to specify the type of objects that you will put into
a tuple.
- You cannot change the elements of a tuple once created or add/remove
elements from it.
- Appear to offer a slight performance and memory allocation improvement
over equivalent lists.
- Ideal for storing a series of values that you want to access, but not 
change.  
- Many ways to create one:
    - `my_tuple = tuple(iterable)`  
    
        > ![Information](../images/information.png) What does `iterable` 
        > mean?  It means any type of object that be iterated over (or, 
        > looped over if you prefer).  Functions or constructors like
        > `tuple` that take iterables do the looping internally to pull 
        > out the elements one by one.
    - my_tuple = (1, 2.5, "string", etc)
    - my_tuple = 1, 2.5, "string", etc

### [Ranges](https://docs.python.org/3.5/library/stdtypes.html#ranges)
- Represented internally as `range`.
- Only holds integers as members.
- Uses less memory than an equivalent tuple/list.
- Three creation forms:
    - `my_range = range(stop)`
    - `my_range = range(start, stop)`
    - `my_range = range(start, stop, step)`
    
> ![Information](../images/information.png) You can use negative numbers as 
constructor parameters.  This has interesting effects.  Try it out and see what 
you can come up with.

### [Strings](https://docs.python.org/3.5/library/stdtypes.html#text-sequence-type-str)
Technically, a string is a sequence of values that represent 
Unicode code points. Practically, they are a sequence of characters.
- Represented internally as `str`
- Two creation forms:
    - `my_string = "Here is my string."`
    - `my_string = str("Here is my string.")`
- Each element of the string is itself a string object.
- You can with either single or double quotes, but can not mix them:
    
    ```python
    >>> string_1 = "double-quoted string"
    >>> string_2 = 'single-quoted string"
    >>> broken_string = "You can not do this.'
    SyntaxError: EOL while scanning string literal
    ```
- You can however, nest single quotes inside of double-quotes or vice-versa:

    ```python
    string_1 = 'He said, "That is really cool!"'
    string_1 = "She said, 'That is uber cool!'"
    ```
    
    > ![Checklist](../images/reminder.png) If you need to nest a single inside
    > of a single quoted string or a double quote inside of a double quoted
    > string, you have to escape them with the `\` character.
    > `string_2 = 'Dog said, "That\'s really tasty!"'`
- Unlike other sequence types, it can only hold other objects of its own type.
- Strings have a [lot of methods](https://docs.python.org/3/library/stdtypes.html#string-methods) 
not shared by other immutable types.  