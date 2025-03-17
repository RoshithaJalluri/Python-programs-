s=input()
str=s.upper()
print(str)
rev=str[-1: :-1]
if rev==str:
    print("palindrome")
else: 
    print("not a palindrome")
