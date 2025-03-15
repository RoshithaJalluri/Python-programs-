a=input()
b=input()
if(a=='rock' and b=='scissor'):
    print("winner is a")
elif(a=='rock' and b=='paper'):
    print("winner is a")
elif(a=='paper' and b=='scissor'):
    print("winner is b")
elif(a=='paper' and b=='rock'):
    print("winner is b")
elif(a=='scissor' and b=='paper'):
    print("winner is a")
elif(a=='scissor' and b=='rock'):
    print("winner is a")
elif(a=='rock' and b=='rock'):
    print("tie")
elif(a=='scissor' and b=='scissor'):
    print("tie")
elif(a=='paper' and b=='paper'):
    print("tie")
