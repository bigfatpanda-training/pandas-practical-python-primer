# Vagrant
[Vagrant](http://www.vagrantup.com) is a tool that creates uniform development 
environments (virtual machines) that can be shared amongst team members.  
In other words, it is a way of getting an identical development setup on all 
computers, regardless of the underlying OS (Windows/Mac).

We will be using it to create a uniform environment to learn Python in our
class. This allows us to focus on Python rather than various environment
differences.

## Prereqs
* Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
* Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads). 

    > ![Information](../images/information.png)  Vagrant can also work with
    other VM providers like VMWare. For class however, we'll be Virtualbox
    because it is **free**. Cha-Ching!
    
## Microsoft Warning
I've seen problems using Vagrant on, ahem, older PCs.  So, if you've got
an older PC, you should plan on spending a little extra time here. I've never 
seen one that couldn't be fixed with some TLC, but just an FYI.

## How It Works
Vagrant uses a special file, rather boring called `Vagrantfile` to create
development VMs.  Teams write and then share Vagrantfile(s) with each other
so that all team members can have an indentical environment to work from.

We'll be doing the same thing here.
    
## Training Steps
1. Take a look at `Vagrantfile` at the root directory of the class folder.
    - It's written in Ruby (lame) but not too hard to understand.
    - The `config.vm.box` variable specifies the "base image" that we'll be 
    using.  A base image is just a bare OS without anything added to it.  We'll
    get to the adding stuff in a bit.
    - 

  * In the root folder of this repository is a `Vagrantfile` for everyone to use during class.
  * Use the `vagrant up` and `vagrant ssh` to get to the command line of your VM.
  * It gives us a clean install of an Ubuntu 14.04 VM but does install some requisites that will be needed for our work - namely some development libraries and Git.  If you need to go back in the future and see what it installed (for your own work!) you can see in the [supplemental provision shell script](../misc/vagrant-pyenv-prereqs.sh)