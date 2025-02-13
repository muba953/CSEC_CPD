x=int(input())
p=input()
m=1
for i in range(x-1):
    z=input()
    if p==z:
        p=z
    else:
        m+=1
        p=y
print(m) 