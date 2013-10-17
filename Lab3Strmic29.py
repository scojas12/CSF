#Micah Stringham
#Strmic29
#October 17th, 2013
#to find the nth integer in a fibonacci sequence impute fibonnacci
#to find the sum of three times the integers, to the nth interger impute sum

series = "fibonacci"
n = 7
print series
if series == "fibonacci":
    x = 1
    y = 1
    for f in range(n-2):
        s = y + x
        x = y
        y = s
    print "the",n,"th","number in the fibonnacci sequence is",y
elif series == "sum":
    s = 0
    m = n
    for a in range(n):
        s = n*3 + s
        n = n - 1    
    print "three times the summation of",m,"is",s
else:
    print"invalid string"

                
    
    