a = int(input("enter the no:"))
b=[]
c=[]
for i in str(a):
    b.append(i)
for i in reversed(str(a)):
    c.append(i)
if b==c:
    print("true")
else:
    print("false")