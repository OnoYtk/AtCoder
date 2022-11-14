import copy
s = input()
l = len(s)

dp = [[0]*9]*(l+1)

for i in range(l+1):
    dp[i][0] = 1

t = "chokudai"
for i in range(l):
    dp[i] = copy.deepcopy(dp[i])
    for j in range(8):
        if s[i] != t[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % (10**9+7)
print(dp[-1][-1])