

a= 121
b=a

rev=0 

while a>0:
    rev=rev*10+a%10
    a//=10
    
if b==rev:
    print("Palindrome")