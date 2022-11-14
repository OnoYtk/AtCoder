n = int(input())
ans = 0

if n < 105:
    ans =0
elif 105==n:
    ans +=1
elif 105 < n:
    ans +=1
    for s in range(106, n+1):
        count = 0
        if s % 2 ==1:
            for t in range(1, s+1):
                if s%t==0:
                    count += 1
            if count == 8:
                ans +=1


print(ans)