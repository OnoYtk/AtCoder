import bisect
n, x=map(int, input().split())
l = list(map(int,input().split()))
for i in range(n-1):
    l[i+1] += l[i]
#print(l)
print(bisect.bisect_left(l,x+1)+1)