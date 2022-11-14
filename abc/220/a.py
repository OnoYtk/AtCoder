a,b,c = map(int,input().split())
ans = -1
for i in range(1,1001):
    if c * i <=b and c*i >=a:
        ans=c*i
        break
print(ans)