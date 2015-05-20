# Save Your Job! Use pyenv!
A sure way to elicit gasps of horror from a **Pythonista** is to run multiple 
python programs in a single environment.  

Practically, what is meant by an Python _environment_ is an interpreter
and the 3rd party modules that you've installed and made available to it.

Almost always, each Python program that you run should have a separate 
environment.  

### Why? Because you want to avoid _dependency hell_.
This sad state of affairs is cause when multiple programs use the same
environment and during an update to one of the programs a 3rd-party module
is upgraded (let's say from v1.5 -> v2.1) to meet a new use-case.

But (shock!), one or more of the other programs depended on how v1.5
did things and don't understand how to work with v2.1.  

**Result:** Programs break mysteriously, kittens die, you lose your job.

Don't do it.

### Training Steps
1. Visit the [pyenv Github repo](https://github.com/yyuu/pyenv).
2. Follow the link to the pyenv installer script and execute the command it gives you.
3. See where this is installed: `/home/vagrant/.pyenv`
4. Demonstrate how to create a virtual environment.



