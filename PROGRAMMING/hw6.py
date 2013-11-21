
#Problem 3 (Comparisons as Boolean Expressions) 

#Define a function (call it anything) that returns 
#a number(either an integer or a float). 
a = 0
b = 0
c = 0
x = 0
d = 0
y = 0
def f(a,b,c):
   d = float((b**2 - 4*a*c)) 
   y = float((-b + d) / (a + a))
   print 'the roots are',y
   x = float((-b - d) / (a + a))
   print 'and',x
   return x
f(1,-2,1)
#Call this function, and compare its return 
#value to another number (either an integer or a float). 
#Assign the value of this comparison to a
#variable called result. Do this using the 
#syntax: result = (a == b), but substituting your
#expression of the previous part as a or b. 
#Print the type of the variable result. 
result = (x == y)
print 'are the roots the same? it is',result
#What is it? Answer this in English in the comments of your code. 
#Try a different comparison, this time between strings.
#Write two comparisons, between string literals that
#should be equal and those that should be false, and print out the 
#type and the value of their comparisons. 
#Are your answers the same for comparing numbers
#as comparing strings? Would they be the same for any other types?
#Answer this in English in the comments of your code. 

x = ("string" == "ham")
y = ('ham' == 'ham')
print 'x is',x
print 'y is',y

#comparing a number to a string will always be false unless
#that string were assigned as a varible to an equivalent expression

#Problem 4 (Calling Functions) 

#Define a function (call it anything) that
#returns a number(either an integer or a float). 
n = 2
def sqrd(n):
    m = n*n
    print n,'squared is',m
    

#Call this function and store its
#return value in a variable called a 
sqrd(2)

#Compare the return value of this function 
#call to a number literal (like 22), and assign the value
#of this comparison to a new variable d 




#Problem 5 (Assignment)

# Write code that assigns a number (like 22)
# to a variable named x using one equals sign (=). 
x = 13
#Write code that receives
#the value of the assignment,
#using similar syntax to this: y = (x = 22). 
y = (x == 13)
print 'is x thirteen? it is',y
z = (x == 'blah')
print 'because x is',x
#the values of y and z will always be the same if x = 13,
#but if x changes to "blah", their values will switch

#Problem 6 (Equality) 
#Write code that assigns value of an equality
#comparison between two integers to a
#variable called w, like this: w = (1 == 2). 
w = (1 == 2)
#Print the value of w. Is this what you expected? 
print 'w is',w
#In a separate line of code, after the ones above,
#write another assignment to w using two different
#values in order to get a different value
#for w than you got above.Print out this new value of w. 
w = (1 == 1)
print 'this w is',w
#Answer in English in the comments the difference between 

# "==" compares two espressions for equivalency

# Problem five asks for the code that "recieves the value
# of the assignment"; which we found doesn't exist in python
# the closest idea is the equality that problem six teaches

