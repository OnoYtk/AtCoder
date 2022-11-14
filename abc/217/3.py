n = int(input())
x = list(map(int, input().split()))
a = [0]*n
#231
#312
for i in range(n):
    a[x[i]-1] = i+1
print(*a)