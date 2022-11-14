S, T = map(int, input().split())

ans = 0
for a in range(S + 1):
    for b in range(S + 1):
        for c in range(S + 1):
            x = a + b + c
            y = a * b * c
            if x <= S and y <= T:
                ans += 1
print(ans)
