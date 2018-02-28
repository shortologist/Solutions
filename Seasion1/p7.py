n,a=map(int,input().split())
x=input().split()
ans=0
if a>n//2:
    x=x[::-1]
    a=n-a+1
for i in range(a-1,n):
    if x[i]=='1' and i+1<2*a:
        if x[a-(i+1-a)-1]=='1':
            ans+=2
    elif x[i]=='1':
        ans+=1
print(ans-int(x[a-1]))