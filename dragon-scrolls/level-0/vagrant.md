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
    - The `config.vm.network` entry allows us to map a virtual port to an 
    actual port on your host system.  We'll use this later in the course
    when we are building websites.
    - The 3 entries of `config.vm.provision` reference files in the `system-setup`
    directory that will be run after the system is booted that install 
    all the necessary dependencies for us to do our work.
    
    > ![Homework](../images/reminder.png) Check out the files in the 
    `system-setup` directory.  They are all shell scripts that Vagrant 
    runs to provision(setup) the machine.  Can you figure out what they
    are doing?

2. Create your virtual machine by running `vagrant up`.
    - This operation will take a significant amount of time the first time 
    you run it because the system has to download the OS image.  The 
    time that this takes will be largely dependent on your network speed.
    
3. Log in to the machine by executing this command: `vagrant ssh`.  Is this
doesn't work, the system failed to build.  Wah wah.  We'll have to work
together on this because your system is probably "special".
    - You should get a new prompt that looks like this: `vagrant@vagrant-ubuntu-trusty-64:~$`

4. Run the following tests to make sure everything is working correctly:
    - `pyenv`: Should display something.
    - `dragon-warrior`: Should take you to `/vagrant/training` directory.
    - `git`: Should display something.