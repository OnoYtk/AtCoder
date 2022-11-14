import bisect
n,m,x = map(int, input().split())
a = list(map(int, input().split()))
cost = bisect.bisect_left(a, x)
print(min(cost, m - cost))