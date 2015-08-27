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
an older PC, you might encounter some problems.  I've never seen one that 
couldn't be fixed with some TLC, but just an FYI.
    
## Command Cheatsheet

  * `vagrant up`: 
    * Will create a VM from a `Vagrantfile`.  To make it easy
      for yourself, make sure you are in the directory where the file 
      exists before issuing the command.
    * Also used to restart a VM that you have stopped using 
    `vagrant suspend` or `vagrant halt`.

  * `vagrant ssh`: Will SSH into your VM. This basically means that you
  get a terminal window for your VM.

  * `vagrant suspend`: Stores the entire state of the VM (including memory)
  and stops the VM.

  * `vagrant halt`: Stores the hard-drive state of the VM and stops it.

  * `vagrant destroy`: Obliterates the VM and all contents.
  
## Training Steps

  * In the root folder of this repository is a `Vagrantfile` for everyone to use during class.
  * Use the `vagrant up` and `vagrant ssh` to get to the command line of your VM.
  * It gives us a clean install of an Ubuntu 14.04 VM but does install some requisites that will be needed for our work - namely some development libraries and Git.  If you need to go back in the future and see what it installed (for your own work!) you can see in the [supplemental provision shell script](../misc/vagrant-pyenv-prereqs.sh)