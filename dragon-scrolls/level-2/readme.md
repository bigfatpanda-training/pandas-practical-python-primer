![Welcome to Level 2](http://images2.fanpop.com/image/photos/12400000/Kung-Fu-Panda-kung-fu-panda-12434029-960-424.jpg)
# Level Two: Command Line Interfaces
A CLI, or **command line interface**, is a program that exposes 
its functionality via the command-line.  I know, what a shock.

We've already been using a very sophisticated CLI - Vagrant.  In this level 
of our training, you'll be learning to create your very own CLIs.  We are going
to do it twice.  The first time using the `argparse` module of the standard
library and then with the `click` third party library.

## Training Setup
- [Grab the latest class updates](../level-0/git-merging-upstream-changes.md) 
**and** push them into your remote repository.
- Submit pull requests with you latest homework assignment.
- - [Setup a new project in PyCharm](../level-0/pycharm-project-setup.md).

## Training Topics
* Unanswered questions from level 0
* Quick Hits
  * Snacks and break schedule. 
  * Git: Upstream Repositories
    * Add the original bigfatpanda-training repo as an **upstream repo**: ``  
    * Grab the latest changes from the upstream remote: `git fetch remote`
    * Merge those changes into your **master** branch: `git merge upstream/master`
* Python
  * There is no spoon.  Everything is an object in Python.
    * Helpful methods for object inspection: `dir()`, `__dict__()`, `help()`
  * A brief overview of common [built-in types](https://docs.python.org/3.4/library/stdtypes.html): `str`, `tuple`, `list`, `dict`, `int` 
  * An [introduction to CLIs](cli-basics.md) based on the standard library.
  * Understanding and improving a standard library based CLI
  * Replicating the CLI with a 3rd Party Package: Docopt or Click
  
