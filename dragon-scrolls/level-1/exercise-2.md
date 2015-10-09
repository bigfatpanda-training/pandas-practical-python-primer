[Previous](exercise-1.md) |  [Next](exercise-3.md)
### Exercise 2: Let's Prove Exercise #1
Alright.  Let's pick one of the basic objects in Python to demonstrate what
we stated in exercise #1.  We will use a **list**. 

Ok.  So let's see what we can do with this thing!

#### Instructions:
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
    >>> my_cool_list.append('When was the last time he took a bath?')
    >>> my_cool_list
    ['I hate Panda.', 'When was the last time he took a bath?']
    ```
    
    > ![Important](../images/information.png) You can find out most of 
    the other methods and attributes an object has by passing the object
    to the `dir()` or `help()` functions.  See what happens when you do
    that.

- Now our object has some interesting attributes.  Namely, the data
that we just put into it.  It gives you a summary of that data when you poke
it like we did, but Python also gives you the ability to access individual 
attributes of lists by specify their index value like so.
    ```python
    >>> my_cool_list[0]
    'I hate Panda.'
    >>> my_cool_list[1]
    'When was the last time he took a bath?'
    ```
    
    > ![Question](../images/question.png) Why does `my_cool_list[0]` give
    you the first element of the list?
    
#### There Is No Secret Ingredient
In "There Is No Secret Ingredient" sections, you'll be given a series of
steps to take on your own.  Doing them will greater help solidify your
understanding of the concepts being taught.  This is where you prove if 
you really want to be a Dragon Warrior.

1. Assign a new list object to the `my_cool_list` name.
1. Add at least 5 entries to it.  You can use both strings (ex.`'example'`) 
or numbers (ex. `123`).
1. Access various members of your list via their index positions.
1. What methods can you use to rearrange the order of the list elements?
1. Figure out how to remove items from your list.  How many are there?


