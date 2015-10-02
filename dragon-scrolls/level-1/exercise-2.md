[Previous](exercise-1.md) |  [Next](exercise-3.md)
### Exercise 2: Let's Prove Exercise #1
Alright.  Let's pick one of the basic objects in Python to demonstrate what
we stated in exercise #1.  We will use a **list**. 

Ok.  So let's see what we can do with this thing!

#### Training Steps:
- In your terminal window type `level-1` to get to the right directory.
    
    > You can't normally type level-1 to get to a directory like this, but
    > I've sprinkled a little Panda magic on the system to makes it easier 
    > for you to move around without getting lost.
    
- Your terminal window should get this prefix at the front `(dragon-warrior)`
which means that your Python virtual environment has been activated.  It's
another bit of Panda magic that I'll explain later.

- Sweet!  Start up the Python interpreter: `python`
- Get yourself a shiny new list object like this: `my_cool_list = list()`
    - Let's talk for a minute about what this statement does.  The stuff on
    the left side of the equals sign is a name. It could be almost anything 
    and it's totally up to you *(although some names are lame and will make 
    all the cool Python kids look down on you)*.  **WAT? There's a cool kids group?!**
    - The stuff on the right side of the equals sign asking Python to create
    a new list object.
    - The equals sign (`=` in case you forgot) tells Python to make the name
    on the left side point to the thing being created on the right side.  So
    whenever you type `my_cool_list` you'll actually be interacting with 
    the thing you made on the right hand side!
    
- Alright, let's poke it and see what happens: 
    ```python
    >>> my_cool_list
    []
    ```
    
- **Yeeaaahhhh, that was underwhelming.**  But still valuable.  You see those
square brackets with nothing inside?  That's Python's way of saying, "this
is an empty list".

- Ok. So let's try using one of those **methods** we said objects had.  One
method that a list object has is the `append` method which you can use to 
add something to the list.  Let's do that and then just poke it again to see
what happens:
    ```python
    >>> my_cool_list.append('I hate Panda.')
    >>> my_cool_list
    ['I hate Panda.']
    ```

So, whenever we are talking about a object(thing) in Python, we can ask
these two questions: 
- What are it's characteristics (attributes)?
- What can it do (methods/functions)?
