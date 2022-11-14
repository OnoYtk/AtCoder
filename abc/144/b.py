n = int(input())
ans = "No"
if n > 81:
    ans = "No"
#elif(n%9==0) or (n%8==0) or (n%7==0) or (n%6==0) or (n%5==0) or (n%4==0) or (n%3==0) or (n%2==0) or (n%1==0):
else:
    for i in range(10):
        for j in range(10):
            if n == i*j:
                ans = "Yes"
                break

print(ans)