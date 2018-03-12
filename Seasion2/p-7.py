while True:
    try:
        ans,l,r=0,0,-1
        s=input()
        for i in range(len(s)):
            x = ord(s[i])
            if x >= 65 and x <= 90 or x >= 97 and x <= 122:
                r=i
            else:
                if r>=l and r!=-1:
                    ans+=1
                l=i+1
        if r >= l and r != -1:
            ans += 1
        print(ans)
    except EOFError:
        break