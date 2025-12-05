x = input("enter a string")
y = input("enter another string")
if sorted(x) == sorted(y):
    print("it is a anagram")
else:
    print("it is a not anagram")