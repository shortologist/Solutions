n=int(input())
a=[]
for i in range(n):
    x=list(map(int,input().split()))
    t=max(x[:i]+x[i+1:])
    while t in a:
        t+=1
    a.append(t)
for i in range(len(a)):
    print(a[i],end=' ')
print()