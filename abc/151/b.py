n, k, m = map(int, input().split())
a = list(map(int, input().split()))

x = m*n - sum(a)
if x <= 0:
    x = 0
elif x > k:
    x = -1

print(x)    