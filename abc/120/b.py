a, b, k = map(int, input().split())
ans = []

if a>=b:
    for i in range(1,b+1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
elif a<b:
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            ans.append(i)

print(ans[-k])