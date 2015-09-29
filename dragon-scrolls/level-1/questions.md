# Questions from Level 0
Here are a list of questions that came up during our first training sessions that I thought needed additional explanation (or that my answer during class was lame..."Uh, I don't know.")

## Can you declare a function/method before using it?
It depends on what we mean by "using it".  To be precise, you can't **execute** a function but you can **reference** it in other definitions.

For example this wouldn't work because it attempts to call(execute) the function before it is defined:

```
# Non-Working Code
break_me = my_function()
print(break_me)

def my_function():
	return "If only I was usable code..."
	

# Output
Traceback (most recent call last):
  File "/vagrant/trainee-area/level-0-example/level_0_example/question_1.py", line 1, in <module>
    break_me = my_function()
NameError: name 'my_function' is not defined

```

On the other hand, the next example would work, even though there is a reference to `my_second_function` inside of `my_first_function` before the function definition.  

The reason that it works in this case is that the definition of `my_first_function` doesn't actual attempt to execute `my_second_function`.  It just sets a reference that will be looked-up later when in `my_first_function` is executed in line 7.

```
# Working Code
1 def my_first_function():
2     return my_second_function()
3
4 def my_second_function():
5     return "Now I am usable code!"
6	
7 dont_break_me = my_first_function()
8 print(dont_break_me)


# Output
Now I am usable code!

```