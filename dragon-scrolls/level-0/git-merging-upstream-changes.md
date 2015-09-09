# Merge Upstream Changes and Rebuild the VM
Github remembers the original repo that you forked from, but your local 
system doesn't.  

This is a problem because often times the owner of the original repository 
will make changes that you'll want to incorporate.  So we need to tell your 
local system about this relationship by creating an "upstream" repository.

## Establishing an Upstream Remote Repository 
This is easy and you only have to do it once:
    - Open your terminal window.
    - `git remote add upstream https://github.com/bigfatpanda-training/pandas-practical-python-primer.git`

## Grab and Merge Changes from the Upstream Remote Repository 
- Open up a terminal window (on Mac) or Git Bash (or Windows)
- Go to your pandas-practical-python-primer folder. 
- Get the latest changes that I've made to the class files from Github:
    - `git fetch upstream`: This gets the changes.
    - `git merge upstream/master`: This merges my changes into your local copy, making them available for you use`
