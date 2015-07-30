# System Setup
Before we begin, we'll need to get some software onto our machines to write
our code and someplace to test it.

### Using a Virtual Machine
In the vast majority of circumstances, the Python code that you write will
eventually run on some flavor of Linux.

Because of this (and because debugging Windows issues is enough to drive you
mad) we'll all be using an Ubuntu virtual machine to run the code that you
create and the class examples.

You have a few different choices for how you want to approach this:

1. Use Vagrant to create a local VM.
2. Create a Ubuntu VM in AWS using a personal account.
3. Utilize nitrous.io to create an VM that is accessible via their console.

Each of these methods has positives / negatives and all of them will take a
little bit of time to get setup.
  
The most complex is the using AWS, and if you want to go that route, you'll
probably need a significant amount of previous experience to know how to 
create the instance, connect to it, etc.

Link to Vagrant Setup
Link to Nitrous IO Setup

### Installing PyCharm
Using an IDE **can** be very helpful.  Particularly for beginners, they
can be immensely time saving - primarily because of the code completion
that they offer.

I strongly suggest that you use the most popular Python IDE, [PyCharm](https://www.jetbrains.com/pycharm/).
That's the tool that I'll be using in class and it's got some great features
that will really help you as your are getting started with Python.

There are multiple editions of the tool offered.  For our class, I suggest
that you download a trial of the professional edition if you didn't receive
a key already.  The open-source version is quite versatile, but it does lack
support for remote interpreters, which we will be using. Don't worry about 
what a remote interpreter is ;)