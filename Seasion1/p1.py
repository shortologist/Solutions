def fun(a):
    for i in range(1,len(a)):
        a[i]+=a[i-1]
    return a
n=int(input())
q1=[0]+list(map(int,input().split()))
q2=sorted(q1)
q1=fun(q1)
q2=fun(q2)
n=int(input())
for i in range(n):
    t,x,y=map(int,input().split())
    if t==1:
        print(q1[y]-q1[x-1])
    else:
        print(q2[y] - q2[x - 1])