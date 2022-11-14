n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

for i in range(n):
    x -= a[i]
    if x < 0:
        break
    elif x == 0:
        i += 1
        break

print(i)