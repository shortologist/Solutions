n,m=map(int,input().split())
d=[False for i in range(100000)]
print()
s=0
arr = []
for i in input().split()[::-1]:
    s += int(not d[int(i)-1])
    print(s,i)
    d[int(i)-1] = True
    arr.append(s)
print(arr)
for i in range(m):
    x=int(input())
    print(arr[-x])