n=int(input())
while n!=0:
    x=input()
    if x[:2]=='on' or x[1:]=='ne' or x[0]+x[2]=='oe':
        print(1)
    else:
        print(2 if x[:2]=='tw' or x[1:]=='wo' or x[0]+x[2]=='to' else 3)
    n-=1