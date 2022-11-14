p = list(map(int, input().split()))
a = list("abcdefghijklmnopqrstuvwxyz")

for i in range(26):
    print(a[p[i]-1], end="")
