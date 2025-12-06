#count inversion in an array
n=[]
count = 0
x = int(input("enter the size"))
for i in range (x):
    l = int(input("enter the numbers"))
    n.append(l)
for i in range (0,x):
    for j in range (i+1, x):
        if n[i]>n[j]:
            count+=1
print(count)