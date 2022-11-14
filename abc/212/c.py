n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
""" 
x = []
for i in range(n):
    for j in range(m):
        if min(x) < abs(a[i] - b[j]):
            break
        else:
            x.append(abs(a[i] - b[j]))
print(min(x)) """
result = 10**9 +7#比較する値を設定
x = 0
y = 0
while x < n and y < m:#aとbの値がすべて取れるような条件の指定
    if abs(a[x] - b[y]) <result:
        result = abs(a[x] - b[y])
    if a[x] < b[y]:
        x += 1
    else:
        y += 1
print(result)