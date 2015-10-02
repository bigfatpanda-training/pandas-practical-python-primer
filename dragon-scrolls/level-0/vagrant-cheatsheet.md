# Vagrant Cheatsheet
Here are the most common commands that you'll be using to operate your 
Vagrant development environment.  You should execute this commands inside
the directory containing the `Vagrantfile`:

  * `vagrant up`: 
    * Will create a VM from a `Vagrantfile`. 
    * Also used to restart a VM that you have stopped using 
    `vagrant suspend` or `vagrant halt`.

  * `vagrant ssh`: Will SSH into your VM. This basically means that you
  get a terminal window for your VM.

  * `vagrant suspend`: Stores the entire state of the VM (including memory)
  and stops the VM.

  * `vagrant halt`: Stores the hard-drive state of the VM and stops it.

  * `vagrant destroy`: Obliterates the VM and all contents.
  
## Rebuilding the Machine
From time to time, you'll find a reason to rebuild the Vagrant VM.  This is 
trivial to do - yeah!  Here's the steps to follow:

- Destroy your old VM: `vagrant destroy`
- Rebuild the VM with new changes: `vagrant up`
- Log into the VM: `vagrant ssh`
- Rule the world!