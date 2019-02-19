# https://codeforces.com/group/EeyLSm275x/contest/235840/submission/50085846
import operator
name = input()
n = int(input())
values = {'posted': 15, 'commented': 10, 'likes': 5}
frindes ={}
for i in range(n):
    s = input().split()
    if s[0] == name:
        if s[3][-2:] == "'s":
            frindes[s[3][:-2]] = frindes.get(s[3][:-2], 0) + values[s[1]]
        else:
            frindes[s[2][:-2]] = frindes.get(s[2][:-2], 0) + 5
    elif s[3][:-2] == name:
            frindes[s[0]] = frindes.get(s[0], 0) + values[s[1]]
    elif s[2][:-2] == name:
        frindes[s[0]] = frindes.get(s[0], 0) + 5
    else:
        frindes[s[0]] = frindes.get(s[0], 0)
        if s[3][-2:] == "'s":
            frindes[s[3][:-2]] = frindes.get(s[3][:-2], 0)
        else:
            frindes[s[2][:-2]] = frindes.get(s[2][:-2], 0)
te = ('', -1)
ind = 0
l = sorted(frindes.items(), key=operator.itemgetter(1, 0), reverse=True)
for i in range(len(l)):
    if l[i][1] != te[1]:
        ii = i - 1
        while ind <= ii:
            print(l[ii][0])
            ii-=1
        ind = i
    te = l[i]
ii = len(l) - 1
while ind <= ii:
    print(l[ii][0])
    ii -= 1