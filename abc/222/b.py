n, p = map(int, input().split())
a = list(map(int,input().split()))
print(sum(x<p for x in a))
