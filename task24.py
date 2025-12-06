#remove spaces in a string
x = input("enter the string")
y = 0
for i in x :
    if i ==" ":
        continue
    else:
        print(i,end="")