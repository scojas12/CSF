# Micah Stringham
# strmic29
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"
a = 1
b = -5.86
c = 8.5408
x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print "of the function: x^2 - 5.86x + 8.5408 the roots are"

print x1,"and", x2


# This uses the quadratic formula to solve for 2 roots when the determinant is 
# greater than 0


###
### Problem 2
###

print "Problem 2 solution follows:"
from hw1_test import *
print a,b,c,d,e,f


# Jason, Brandon, Alex and I all worked together from different google searches


###
### Problem 3
###

print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)
print "((",a," and ",b,") or (not ",c,") and not (",d," or ",e," or ",f,"))"
print "is",((a and b) or (not c) and not (d or e or f)) 

###
### Collaboration
###

# ... Brandon, Jason, Alex and I.
