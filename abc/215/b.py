n = int(input())
k = 0
for i in range(200):
    if 2**i <= n:
        k = i
    else:
        break
print(k)