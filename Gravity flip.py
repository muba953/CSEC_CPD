 x=int(input())
y=input()
m=list(map(int,y.split()))
n=sorted(m)
for i in range(len(n)):
    print(n[i],' ',end="")
