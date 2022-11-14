'''
n = int(input())
a = [map(int, input().split())]
b = [map(int, input().split())]
c = [map(int, input().split())]
count = 0
for i in a:
    for j in b:
        for k in c:
            if a[i] < b[j] and b[j] < c[k]:
                 count += 1
print(count)
'''
import bisect
N=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
C=sorted(list(map(int,input().split())))
print(sum(bisect.bisect_left(A,b)*(N-bisect.bisect_right(C,b)) for b in B))

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
a.sort()
b.sort()
c.sort()
for mid in b:
    ans += bisect.bisect_left(a,mid) * (n - bisect.bisect_right(c,mid))
 
print(ans)
'''
# data配列の中身を2倍にする
newData = []
for d in data:
  newData.append(d * 2)
# data配列の中身を2倍にする
newData = [d * 2 for d in data]
'''