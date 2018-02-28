while True:
    n=int(input())
    if n==0:
        break
    x=input()
    p,ans=-1,2000000
    if x[0]=='R':
        t=True
        p=0
    elif x[0]=='D':
        t=False
        p=0
    elif x[0]=='Z':
        ans=0
        x=''
    for i in range(1,len(x)):
        if x[i] == 'Z':
            ans = 0
            break
        elif x[i]=='D':
            if p!=-1 and t:
                ans=min(ans,i-p)
            t=False
            p=i
        elif x[i]=='R':
            if p!=-1 and not t:
                ans=min(ans,i-p)
            t=True
            p=i
    print(ans)