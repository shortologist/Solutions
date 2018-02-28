n=int(input())
a=input().split()
t=[0 for i in range(n+1)]
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    t[l-1]+=1
    t[r]-=1
ans,q=0,0
for i in range(n):
    q+=t[i]
    ans+=int(q==0)
print(ans)
q=0
for i in range(n):
    q+=t[i]
    if q==0:
        print(a[i],end=' ')
print()