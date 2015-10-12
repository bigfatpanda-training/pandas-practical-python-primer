[Previous](exercise-2.md) |  [Next](exercise-4.md)
## Exercise 3: Types(Classes) & Their Hierarchies

### Object Types(Classes)
Ok.  So, we've gotten a basic introduction to what **objects** are.  Now 
we are going to discuss the related concepts of Types & Classes.
 
Analogies can be somewhat helpful here. You can think of Classes like 
factories and Objects like the things that they manufacture.  These 
factories are limited in that they (in almost all cases) create one type of 
thing.  

Think of it like a toaster factory.  The toasters may vary slightly (color, 
capacity), but their basic characteristics are all the same because the
come from the same source.

Alternative, you can think of Objects as buildings and Classes and the 
blueprints that they come from.

The core idea is that Classes generate objects of the same kind - that is,
they share common methods and attributes.

> ![Extra](../images/information.png) Now to make things all mind-bending 
> and **Inception-like**, Classes are actually objects themselves! 
> They are just special in that they are objects that create other objects 
> based on the blueprint that the have inside of them.

You've already seen a class in action.  You used it when you created your
lists in the previous exercise:
```python
my_cool_list = list() <- Right Here.  You called the class which created the object!
```

Finally, when an object comes from a class, people say that it's **type** is
the name of the class.  Knowing an object's type tells you what you can
expect as far as methods and attributes.

### Type(Class) Hierarchies
Classes are often arranged in a hierarchical fashion.  Like a family tree, 
characteristics from classes higher up the chart ("parent classes") pass 
methods and attributes down to those lower on the chart ("child classes").
 
The children will resemble each other but also have some differences from 
their siblings and parents.

We'll see how this plays out in our next exercise, where will cover a 
few of the common built-in types that you'll see a lot of during our time
together.