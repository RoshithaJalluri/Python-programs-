#SOLID SQUARE PATTERN 
n=5
for i in range(n):
    print("* "*n)
    

#HALLOW SQUARE PATTERN
n=5
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
    

#RIGHT HALF TRIANGLE 
n=5
for i in range(n+1):
    print("*"*i)


#REVERSE RIGHT HALF TRIANGLE 
n=5
for i in range(n):
    print("*"*n)
    n-=1
    

#LEFT HALF PYRAMID 
n=5
for i in range(n+1):
    print(" "*(n-i)+"*"*i)
    

#REVERSE LEFT HALF PYRAMID
n=5
for i in range(n):
    print(" "*i+"*"*(n-i))


#TRIANGLE
n=5
for i in range(n):
    print(" "*(n-i)+"* "*i)


#REVERSE TRIANGLE 
n=5
for i in range(n):
    print(" "*i+"* "*(n-i))
    

#HALLOW TRIANGLE 
n=10
for i in range(n):
    if i==0:
        print(" "*(n-i)+"* "*(i+1))
    elif i==n-1:
        print(" "*(n-i-1)+"* "*(i+2))
    else:
        print(" "*(n-i-1)+"*"+"  "*(i)+" *")
        
    
#REVERSE HALLOW TRIANGLE 
n=10
for i in range(n):
    if i==0 or i==n-1:
        print(" "*(i+1)+"* "*(n-i))
    else:
        print(" "*i+"*"+"  "*(n-i-1)+"* ")
        
        
#SOLID RECTANGLE 
rows=12
col=8
for i in range(rows):
    print("* "*col)
    
    
#HALLOW RECTANGLE PATTERN
row=5
col=10
for i in range(row):
    if i==0 or i==row-1:
        print("* "*col)
    else:
        print("*"+" "*(2*col-3)+"*")
    print()  
    
    
#RHOMBUS
n=10
for i in range(n):
    print(" "*i+"* "*n)
    
    
#PARALLELOGRAM
row=5
col=10
for i in range(row):
    print(" "*i+"*"*col)


#SQUARE 1 PATTERN
n=5
for  i in range(n):
    print("1"*n)
    
    
#RIGHR ANGLE NUMS PATTERN
rows = 4
num = 1   
for i in range(1, rows + 1): 
    for j in range(i):
        print(num, end=" ")
        num += 1  
    print() 
    
    
#SQUARE NUMS PATTERN
n=10
for  i in range(n):
    for j in range(n):
        print(i,end='')
    print()
    
    
#INCREMENTAL TRIANGLE PATTERN
rows = 4  
col = 6  
for i in range(rows):
    print(str(col) * (rows - i)) 
    col -= 1  
    
    
#REVERSE RIGHT ANGLE PATTERN 
num = 10
rows = 4 
count=4
for i in range(rows):
    for j in range(count):
        print(num, end=" ")
        num -= 1
        if num == 0:
            break  
    print()
    count -= 1  
