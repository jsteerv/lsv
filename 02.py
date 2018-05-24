<<<<<<< HEAD
""".
=======
"""
>>>>>>> 7d1c64f9bd7ec2dffa33b570c9e4aafef585fdd8
Write a program that calculates and prints the value according to the given
formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
<<<<<<< HEAD
C is 50.
H is 30.
D is the variable whose values should be input to
your program in a comma-separated sequence.
=======
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
>>>>>>> 7d1c64f9bd7ec2dffa33b570c9e4aafef585fdd8
Example
Let us assume the following comma separated input sequence is
given to the program:
100,150,180
The output of the program should be:
18,22,24
<<<<<<< HEAD
=======
 
>>>>>>> 7d1c64f9bd7ec2dffa33b570c9e4aafef585fdd8
Hints:
If the output received is in decimal form, it should be rounded
off to its nearest value (for example, if the output received is 26.0,
it should be printed as 26)
In case of input data being supplied to the question, it should be assumed
to be a console input.
<<<<<<< HEAD
"""
from math import sqrt

# variables

C, H = 50, 30
# D = input("Add 3 numbers like: 10,100,522: \n").split(",")
D = "456,10,1".split(",")
ram = 0
output = []

D = [int(i) for i in D]

# list comprehension version

# output = [str(round(sqrt((2 * C * i) / H), 2)) for i in D]
# print(output)

# foor loop version

for i in D:
    ram = sqrt((2 * C * i) / H)
    ram = round(ram, 2)
    ram = str(ram)
    output.append(ram)
    # print(output)

output = ",".join(output)

print("This is output: " + output)
=======
""" 
>>>>>>> 7d1c64f9bd7ec2dffa33b570c9e4aafef585fdd8
