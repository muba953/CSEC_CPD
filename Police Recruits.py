m=int(input())
n=list(map(int,input().split()))
s=0
l=0
for i in n:
    if i<0 and s==0 :
        l+=1
        s=0
    elif i<0:
        s-=1
    else:
        s+=i       
print(l)        