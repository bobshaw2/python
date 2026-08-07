


n=int(input("enter number: "))

sum=0

for i in range (1,n,1):
    if n % i == 0 :
        sum+=i
        
if sum == n:
    print ("t is a square number")
    
else:
    print("it is not a square number")
         
        