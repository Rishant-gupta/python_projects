'''
a=[]
n = int(input("enter the no. of list: "))

for i in range(n):
    a.append(input())
print(a)

b = []
'''
d = []
c = []
a = ("float", "fly", "flash")
for i in a :
    b = list(i)
    c.append(b)
for i in range(len(c)):
    for j in (len(c)):
         if c[i][j] == c[i+1][j]:
              d.append(c[i][j])
print(str(d))
'''
for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] == c[i+1][j]:
            d.append(j)
print(d)
'''



