u=input()
g=u.split()
x=input()
y=x.split()
#z=int(y[0])
k=len(y)
m=0
for i in range(k):
    if int(y[i])<=int(g[1]):
        m+=1
    else:
        m+=2
print(m)            