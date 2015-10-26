# PyCharm Project Setup
For each training level of our program, we'll create a new project inside
of PyCharm. To do this, take the following steps:

> ![Information](../images/information.png) Depending on whether you are on a 
Mac or PC, the names of menu items can vary slightly.  I work primarily on a 
Mac, but will note these differences wherever I am aware of them. 

- Open the class folder as a new project: `File` -> `Open` -> Select `[class-folder]/trainee-area/level...` -> Click `Open/Choose`
    - Make sure that you pick the correct training level.
    - If asked, always choose to open up the project in a new window.
    - You should be presented with an empty editor and a window on the left
    side of the screen showing the files in the directory.
    - If you are presented with a `Unregistered VCS Root Detected` window, you
    can safely ignore it.  Pycharm is complaining because your project folder
    is inside of a larger directory structure that contains a Git root at a
    higher level.  Yes... if that didn't make sense don't feel bad.  Just
    ignore the warning and you'll be fine.
    
- We now need to make a couple of changes to the settings so that everything
works correctly.  The first one is a little tricky, the second one is pretty easy.

## Setting the Project Interpreter Options
You only need to do this step once for class.  In the real world, each 
program would have a separate virtual environment (which Pycharm refers to 
as an interpreter).  However, it can be a confusing step for newcomers, so 
we'll only to it once.
- In the `Preferences`(Mac) or `Settings`(Windows) interface, search for
`Project Interpreter`.  
- If you haven't setup an interpreter before for class:
    - Click the ![Interpreter Icon](../images/pycharm-interpreter-settings-icon.png)
    - Select the `Add Remote` option
    - Fill out the dialogue according to this pattern:      
    ![Project Interpreter Settings](../images/pycharm-interpreter-settings.png)
- If you've already setup an interpreter for class before, just select it
from the list like so:  
![Existing Interpreter Settings](../images/pycharm-existing-interpreter.png)

> ![Gotchas](../images/alert.png) If you've never connected to the Vagrant 
machine before (including if you recently rebuilt it - it's a new machine as
far as Pycharm knows), there might be a dialogue box hiding underneath 
your settings options that you have to respond to before you'll be able to 
put in the `Python interpreter path` after you've specified the 
`Vagrant Instance Folder`.  Just click `Ok`, take care of the underlying 
dialogue box and then come back and continue.

# Setting the Project Structure Options
- Since there are two code folders in each training level (one for your 
stuff and one for my examples) we need to tell PyCharm to use yours or it
will get confused about how files relate to each other.

- Tell PyCharm where your root source code is for this project so that it will
correctly handle code hinting and imports.  You do this in the `project structure`
area of the settings/preferences.  Make sure to indicate that `dragon-warrior`
is marked as a `sources` folder.
![Project Structure Settings](../images/pycharm-project-structure.png)

- While PyCharm is great, there quality control, is frankly sub-standand. 
There are usually a few bugs to content with.  In the latest version, 
there is a bug in the Mac version that doesn't correctly pull the Vagrant
settings from the environment.  To get around this, you have to start
PyCharm from the terminal window with the `charm` command.