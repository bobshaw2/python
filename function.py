def palindrome(st):
    
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]
        
    if st==rev:
        print("palindrome")
    else:
        print("not palindrome")
        
        
palindrome("ruble")
palindrome("naman")