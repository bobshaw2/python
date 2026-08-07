

a="asrs@242324@!#@$^#$%^$%^#^#"

char = 0
digit = 0
spechar = 0

for i in a:
    if i.isalpha():
        char+=1
    
    elif i.isdigit():
        digit+=1
    
    else:
        spechar+=1
        
print(f"no of characters: {char}\n no of digit:{digit}\n no of spechal character:{spechar}")