## Merge Upstream Changes and Rebuild the VM
Remember when you forked the class repo in Github?  That made a copy of the
class materials repository in your personal account which you then downloaded
to your system with the `git clone` command.

In nearly all open-source projects in the wild, there
will often be times that original project makes updates that you want to 
incorporate into your copy. The same is true for our class.  Each week,
I will add some new content to the class repository that you'll need to get
your hands on.

In common Git parlance, this involves **fetching** and **merging** changes
from an **upstream remote**.

Let's define these terms a bit.  Like most things, there are deeper 
(and longer) explanations of these concepts, but this is enough to 
get you going:

- A Git **remote** is a connection between a repo on your machine and 
a repo on another machine (in our case, in Github).  You don't know it yet, 
but when you cloned your version of the class repo to your computer, Git
created a repo named `origin` which is tied to your copy in Github. 

    > ![Alert](../images/reminder.png) On the command line you can 
    verify this by executing `git remote -v` inside your class folder (either
    or your host system or inside the VM).  You'll see that you've got a 
    remote set up that is pointing to a URL in your Github account.
    
- **Fetching** is the term that Git uses when you want to pull the changes
from a remote (I'm simplifying some here) and make them available for use on
your machine.

- **Merging** is the action that you take to well, merge - or incorporate - the
changes that you get with the `git fetch` command into your code files.  Both
fetching and merging and required to incorporate updates from a upstream 
remote into your local working copy.
    
### There Is No Secret Ingredient
1. Create an **upstream remote** that points to the original class repo
by executing this in your terminal & class folder.  Then use the 
`git remote -v` to verify what you've done.  Should look something like this:

    ```bash
    >>> git remote add upstream https://github.com/bigfatpanda-training/pandas-practical-python-primer.git
    >>> git remote -v
    origin	https://github.com/eikonomega/pandas-practical-python-primer.git (fetch)
    origin	https://github.com/eikonomega/pandas-practical-python-primer.git (push)
    upstream	https://github.com/bigfatpanda-training/pandas-practical-python-primer.git (fetch)
    upstream	https://github.com/bigfatpanda-training/pandas-practical-python-primer.git (push)
    ```
    
    > ![Alert](../images/alert.png) You only have to do this part once.  Try
    to do it again and you'll get `fatal: remote upstream already exists`. 

1. Fetch the recent changes that I've made to the class repository: `git fetch upstream`
1. Finally, merge them into your working copy and you're ready to go: `git merge upstream/master`
