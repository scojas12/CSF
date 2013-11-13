# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"



print "1 + 2 + 3 + 4 + 5... + n ="
# where x is the added number and s is the sum, and n is our test varible
from hw2_test import n
x = 0
s = 0
while (x < n):
    x = x + 1
    s = s + x
else:
    print "ANSWER:",s
    print "where n = 100"

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# ... write your code and comments here (and remove this lined

lines = range(2,11)
for x in lines:
  
    print (1.0/x)

    
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"


n = 10
triangular = 0
for i in range(n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# ... write your code and comments here (and remove this line)

n = 10
triangular = 1
for i in range(1,n+1):
    triangular = triangular * i
print "Triangular number", n, "via loop:", triangular


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
triangular = 0
for i in range(1,numlines):
    print i


# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
