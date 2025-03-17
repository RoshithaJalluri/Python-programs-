n=1000
for i in range(1,1001):
    if i % 2 == 0:
        if i%3==0:
            print(i)
        else:
            print("even number,but not a multiple of 3")
    else:
        if i%3==0:
            print(i)
        else:
            print("odd number,but not a multiple of 3")
        
    
