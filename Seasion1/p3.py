t=int(input())
for i in range(t):
    n,hi=map(int,input().split())
    a=[0 for j in range(n+1)]
    for j in range(n):
        l,h=map(int,input().split())
        a[l]+=1
        a[h+1]-=1
    for j in range(1,n):
        a[j]+=a[j-1]
    for j in range(1,n):
        a[j]+=a[j-1]
    a=[0]+a
    m=-1
    for j in range(n-hi+1):
        m=max(m,a[j+hi]-a[j])
    print(n*hi-m) 