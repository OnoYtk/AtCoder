n = int(input())
d = sorted(list(set(int(input()) for i in range(n))))
ans = 0
if len(d) == 0:
    ans = 1
else:
    ans = len(d)
print(ans)