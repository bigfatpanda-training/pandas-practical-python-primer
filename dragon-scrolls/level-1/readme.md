![Welcome to Level 1](http://g-ecx.images-amazon.com/images/G/01/DVD/Paramount/detailpages/KungFuPanda/KungFuPnda_M1L.jpg)
# Level Three: The Zen of Python

## Class Setup
Today we're going to start using Python!  Here are a couple of things
to do before each class:
    - [Grab the latest class updates](../level-0/git-merging-upstream-changes.md)
    - [Rebuild the Vagrant VM](../level-0/rebuild-vagrant-vm.md)

### PyCharm Project Setup
* Open a new project folder: `[class-folder]/trainee-area/level-3/using-web-services`
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
