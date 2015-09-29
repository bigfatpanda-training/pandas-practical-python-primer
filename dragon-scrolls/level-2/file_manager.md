# A Command Line Interface Based on the Standard Library
Today will be looking at a CLI that was written with only the standard
library.  In other words, there are no 3rd party packages in this program.

## Observations of `file_manager.py`
* Can we tell what the program should do by its docstrings and names?
* Structure of the imports.
    * Good: Order
    * Bad: `from AutoFileUtilities import *` introduces magic names.
        * Experiment to find the magic names.
* Naming in violation of PEP8
* Docstrings
    * Good: Present in all public methods and the class.
    * Bad: Not present for the module.  What does PEP 257 say?

### FileManager Class / __init__ Method
* What does the `(Auto_File_Utility)` part of the class signature mean?
* What is `__init__`?
    * It is an object constructor.  It is what takes the class 'blueprint'
    and gives you an actual object.
* Why is `__init__` calling `Auto_File_Utility.__init__`?
* Why do the methods all take [`self` as the first argument?](http://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self-in-python)


#### FileManager.evaluate_command_line_arguments()
* Correct Docstring?
* Look through it, do the names/docs make it understandable?
* Walk through the online documentation for the argparse package.
* Is `parent_parser` the right name for line 34?





