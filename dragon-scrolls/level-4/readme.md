![Welcome to Level 3](http://g-ecx.images-amazon.com/images/G/01/DVD/Paramount/detailpages/KungFuPanda/KungFuPnda_M1L.jpg)
# Level Three: Creating Web Services

## Class Setup

#### Merge Upstream Changes and Rebuild the VM
* Open up a terminal window (on Mac) or Git Bash (or Windows)
* Go to your pandas-practical-python-primer folder. 
Inside of this folder should be your Vagrantfile.
* Get the latest changes that I've made to the class files from Github:
    * `git fetch upstream   # This gets the changes.`
    * `git merge upstream/master   # This merges my changes into your local copy, making them available for you use`
* Destroy your old VM: `vagrant destroy`
* Rebuild the VM with new changes: `vagrant up`
* Log into the VM: `vagrant ssh`
* Go to the class directory: `cd /vagrant/trainee-area/level-3-creating-web-services`
* Leave that terminal/Git bash window open and you'll be ready to go for class!

#### PyCharm Project Setup
* Open a new project folder: `[repo-location]/trainee-area/level-3/using-web-services`
* Set the project interpreter 
![Project Interpreter Settings](level-3-interpreter.png)
* Tell PyCharm where your root source code is for this project so that it will
correctly handle code hinting and imports.  You do this in the `project structure`
area of the settings/preferences.  Make sure to indicate that `trainee-friends-api`
is marked as a `sources` folder.
![Project Structure Settings](level-3-project-structure.png)
* Probably restart PyCharm due to software bug in latest version.

## Training Topics

### Building a Basic Web Service in Python (Day 1)
* There are a number of libraries/frameworks available to build web services in
Python.  The two most popular are [Django](https://www.djangoproject.com/) and [Flask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CB4QFjAA&url=http%3A%2F%2Fflask.pocoo.org%2F&ei=jwyYVdihJ4b0tQW5jbr4Dg&usg=AFQjCNHCF6gYMbnkUKtJl-u3lzTeLt-61A&bvm=bv.96952980,d.b2w).
* We will be using Flask (it's easier to get started with) to build a simple
API that allows use to list, create, update, and even delete a list of our
friends.

### Enhancing our Friends API (Day 2)
* After we get our basic functionality up and running, we'll make some
enhancements to our API that would standard features of a real-world program:
    * A database to hold our friendship info so that it persists between
    program runs.
    * Some sort of authentication requirement so that random people (or 
    machines!) can't change your list of friends.

[Start Training](exercise-1.md)
