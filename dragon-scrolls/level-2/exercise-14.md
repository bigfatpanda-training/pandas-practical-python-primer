##### [Previous](exercise-13.md) |  [Next](exercise-15.md)  

## Exercise 14: `Click` Lab
Use `click` to recreate parts of your current CLI:
 
1. Copy/move/delete file(s) functionality with positional parameters.
1. Refactor the current functionality to take keyword arguments.
    - This will require you implement support for wildcards since `click`
    doesn't support optional/flag arguments with multiple values.
    - Look at the `glob` module.


1. Create an additional CLI that performs the following Git workflows:
    - `git fetch upstream` & `git merge upstream/master`
    - Add all files in a directory, commit them, and push to Origin.
    
 
### Bonus Challenges
 - Use other standard library modules to perform basic file operations 
 instead of `subprocess`
 - Try to "refactor" the common functionality of `copy_files` and `move_files`
 into a separate function.
 - Try a variety of inputs on all your functions and implement error checking.
 - Add support for recursive copy/delete operations.


### Takeaways
- What was it like working with a 3rd Party Library?
- What was good/bad about it?
- What were the tradeoffs?

     
