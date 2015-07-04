[Previous](readme.md) |  [Next](exercise-2.md)
## Program Structure & Setup
#### Step 1: Package Creation / Dependency Installation
* Create a new Python package inside `/trainee-area/level-3/using-web-services`
    * Call it `[your_id]_friendship_api`.
    * If you did this correctly, you'll automatically get an `__init__.py` file
    inside of the folder.
* Add a docstring to `__init__.py` which describes what the entire package 
will provide. In our case, an API to interact with friendship data.
* PyCharm should detect the missing 3rd party libraries specified in 
`requirements.txt` and offer to install them for you. If it does not, then
your interpreter is probably not set up correctly.

#### Step 2: Create Modules inside `friendship_api` Package
* To start off, we'll need two modules (i.e. python files) inside the package:
    * `datastore.py`: This is where we will store information on our friends.
    * `api.py`: This will be the actual Flask API.


   
