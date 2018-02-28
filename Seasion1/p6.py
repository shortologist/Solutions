n,x=map(int,input().split())
ans=0
for i in range(min(int(x**0.5),n)):
    if x%(i+1)==0 and n>=x/(i+1):
        ans+=2
print(ans)