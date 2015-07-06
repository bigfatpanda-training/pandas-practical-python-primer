[Previous](readme.md) |  [Next](exercise-2.md)
## Program Structure & Setup
#### Step 1: Package Creation / Dependency Installation
* Inside the `/vagrant/trainee-area/level-3-using-web-services` directory, you
will see a folder called `trainee-friends-api`.  This is where you will be 
putting your work for this session.

* Note that there are already two files inside of this directory: 
`requirements.txt` and `run_server.py`.
    * `requirements.txt` is the standard way of indicating which 3rd party
    libaries (meaning, those not included in the standard libary) your app
    requires.
    * `run_server.py` is the file we will call at the command line to 
    invoke the testing HTTP server to run our Flask app inside of.  In a real
    production environment, we wouldn't use the testing server and this file
    wouldn't be necessary, but using it will help us get started quickly.

* Create a new Python package inside `/trainee-area/level-3-using-web-services/friends-api`
    * Call it `trainee_friends_api`.
    * If you did this correctly, you'll automatically get an `__init__.py` file
    inside of the folder.

* Add a docstring to `__init__.py` which describes what the entire package 
will provide. In our case, an API to interact with friendship data.

* PyCharm should detect the missing 3rd party libraries specified in 
`requirements.txt` and offer to install them for you. If it does not, then
your interpreter is probably not set up correctly.

#### Step 2: Create Modules inside `friends_api` Package
* To start off, we'll need two modules (i.e. python files) inside the package:
    * `datastore.py`: This is where we will store information on our friends.
    * `api.py`: This will be the actual Flask API.


   
