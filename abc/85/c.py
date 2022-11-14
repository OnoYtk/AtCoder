n, y= map(int, input().split())
a,b,c = -1,-1,-1
for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        if 10000*i + 5000*j + 1000*k == y and i+j+k == n:
            a,b,c = i,j,k

print(str(a)+" "+str(b)+" "+str(c))