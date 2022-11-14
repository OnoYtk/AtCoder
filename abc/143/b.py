n = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        ans += d[i]*d[j]
        
print(ans)

#ans = d[0]*d[1] + d[0]*d[2] + d[1]*d[2]