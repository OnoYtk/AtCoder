"""""""""""TLE
q = int(input())
p = [list(map(int, input().split())) for i in range(q)]
x = []
ans = []
for i in range(q):
    if p[i][0] == 1:
        x.append(p[i][1])
    elif p[i][0] == 2:
        x = list(map(lambda y: y+int(p[i][1]), x))
    elif p[i][0] == 3:
        ans.append(min(x))
        x.remove(min(x))

for i in range(len(ans)):
    print(ans[i])
"""
import heapq
q = int(input())
sack = []
heapq.heapify(sack)
total = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(sack, query[1] - total)
    elif query[0] == 2:
        total += query[1]
    else:
        ans = heapq.heappop(sack)
        print(ans + total)