[Previous](exercise-7.md) |  [Next](exercise-9.md)
## Exercise 8: Decoding our CLI's Output
1. Expect exercise-7 output.
1. Code snapshot.
1. Text coming into the program from outside is in bytes.  Encoded to UTF-8.
Must be decoded.
1. Furthermore, let's strip the `\n` off the end of each copy operation
result.
1. Talk about when/when not to specify default arguments.
1. Revisit method chaining.

python stdlib_cli.py -f testfile_1 testfile_2 -d /home/vagrant
b'\xe2\x80\x98testfile_1\xe2\x80\x99 -> \xe2\x80\x98/home/vagrant/testfile_1\xe2\x80\x99\n'
b'\xe2\x80\x98testfile_2\xe2\x80\x99 -> \xe2\x80\x98/home/vagrant/testfile_2\xe2\x80\x99\n'