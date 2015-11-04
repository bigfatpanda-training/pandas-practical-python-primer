##### [Previous](exercise-10.md) |  [Next](exercise-12.md)  

## Exercise 11: Going Multi-Platnum
[Code Files](../../training/level-2-command-line-interfaces/bfp-reference/exercise_10)

We've made great progress thus far.  Now let's take the next step
and turn our CLI into something that can handle more than one type of task.  
Specifically, let's add the ability for our program to move files as well as 
copy them.

1. Add subparsers to your argparse.Argument parser object.  Talk about what
this is doing to the object.  
    ```
    subcommand_parsers = parser.add_subparsers(
            title="Available Commands",
            description="The following sub-commands are available.",
            dest="command")
    subcommand_parsers.required = True
    ```
    
    * Objects have attributes which are themselves objects.
    * What does `self._subparsers` mean?  `self` and "private" attributes.
    
2. Create two subparsers for the `move` and `copy` commands.
    ```
    copy_parser = subcommand_parsers.add_parser(name='copy', help="Copy Files")
    move_parser = subcommand_parsers.add_parser(name='move', help="Move Files")
    ```
    
    * Temporarily comment out the all of the `parser.add_argument` calls
    and see how the program now looks from the command line.
    
3. Add the `parser` arguments to both `move_parser` and `copy_parser`.
    * See how this affects the program operation.
    * Pay attention to how code is being repeated here.  This is a bad
    thing.  Violation of DRY.  We'll come back to it later if we have time.

     