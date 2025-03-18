n=0
while n<=100:
    if n%2==0:
        if n%4==0:
            print(n)
        else:
            print("even,but not a multiple of 4")
    else:
        if n%3==0:
            print(n)
        else:
            print("odd,but not a multiple of 3")
    n+=1
            
