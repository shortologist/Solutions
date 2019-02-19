# https://codeforces.com/group/EeyLSm275x/contest/235840/problem/A
n, k = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
ans, ind, kt = [-1, -1], 0, 0
for i in range(n):
    kt += l[ind] - l[i]
    while kt > k:
        ind += 1
        kt -= (l[ind - 1] - l[ind]) * (i - ind + 1)
    if (i - ind) + 1 >= ans[0]:
        ans[0], ans[1] = (i - ind) + 1, l[ind]
print(ans[0], ans[1])