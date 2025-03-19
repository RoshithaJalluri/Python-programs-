#SOLID SQUARE PATTERNS

n=10
for i in range(n):
    print("* " * n)

#SOLID RHOMBUS PATTERN 

n=10
for i in range(n):
    print(" "*i + "* " * n)

#HALLOW SQUARE PATTERN

n=10
for i in range(n):
    if i==0 or i==(n-1):
        print("* "*n)
    else: 
        print("* " + "  "*(n-2) + "*")

#RIGHT ANGLE TRIANGLE OR RIGHT PYRAMID 

n=10
for i in range(n):
    print("* "*i)

#REVERSE PYRAMID 

n=5
for i in range(n):
    print("* "*n)
    n=n-1

#LEFT HALF PYRAMID 

n=10
for i in range(n):
    print(" "*(n-i)+"*"i)


#REVERSE PYRAMID 

n=10
for i in range(n):
    print(" "*i+"*"*n)
    n=n-1


#HALLOW TRIANGLE 

n=10
for i in range(n):
    if i==0 or i==n-1:
        print(" "*(n-i)+"* "*(i+1))
    else:
        print(" "*(n-i-1)+"*"+"  "*(i)+" *")







    

