[Previous](exercise-6.md) |  [Next](exercise-8.md)
## Exercise 7: Importing `file_io` and Delegating To It
In this exercise we'll attempt to actually copy some files.  
**Awesome!**

Before we get started, you'll need to make a small change to your 
project configuration settings in PyCharm since you are now working
in a subfolder of `dragon-warrior`.  

1. Go to the project settings/preferences.
1. Search for Project Stucture and change the sources folder
to be your subfolder.

### There Is No Secret Ingredient: Copying Files
1. In your subfolder, create a couple of dummy test files: `testfile_1` and 
`testfile_2`.
2. Add a line of text to each of those files.
3. `import` your `file_ops` module.
4. Add a call to `file_ops.copy_files` at the bottom of your script and 
pass it `program_arguments.filenames` and `program_arguments.destination`
as the two parameters.
5. Get rid of the `print` statement that outputs the program arguments from
your parser's `parse_args()` method.  We don't really need it anymore.
1. Update module docstring since you now have a module that does something.
6. Try to copy your test files to `/home/vagrant`.

python stdlib_cli.py -f testfile_1 testfile_2 -d /home/vagrant
b'\xe2\x80\x98testfile_1\xe2\x80\x99 -> \xe2\x80\x98/home/vagrant/testfile_1\xe2\x80\x99\n'
b'\xe2\x80\x98testfile_2\xe2\x80\x99 -> \xe2\x80\x98/home/vagrant/testfile_2\xe2\x80\x99\n'