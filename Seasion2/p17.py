def value(c):
    if c=='+' or c=='-':
        return 0
    elif c=='*' or c=='/':
        return 1
    elif c=='(':
        return -1
    else:
        return 2
t=int(input())
while t:
    l=[]
    ans=''
    for i in input():
        x=ord(i)
        if x>=97 and x<=122:
            ans+=i
        else:
            if i==')':
                ch=l.pop()
                while ch!='(':
                    ans+=ch
                    ch=l.pop()
            elif i=='(':
                l.append('(')
            else:
                ch = l.pop()
                while len(l)!=0 and value(ch)>value(i):
                    ans += ch
                    ch = l.pop()
                l.append(ch)
                l.append(i)
    while len(l)!=0:
        ans+=l.pop()
    print(ans)
    t-=1