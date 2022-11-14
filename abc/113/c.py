l,r =map(int,input().split())
count = 0
for i in range(l,r):
    for j in range(i+1,r+1):
        i=str(i)
        j=str(j)
        if i[-1] == j[-1]:
            count += 1
print(count)