import heapq
n, m = map(int, input().split())
a = list(map(lambda x: int(x)* (-1), input().split()))
#-をかけることで，実質大きいものを取り出せ

heapq.heapify(a)

for i in range(m):
    temp = heapq.heappop(a) *(-1)//2
    heapq.heappush(a, temp*(-1))

print(sum(map(lambda x: -x,a)))