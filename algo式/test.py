n, m = map(int, input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int, input().split())))
ab = sorted(list(set(a) & set(b)))
for i in range(len(ab)):
    print(ab[i])
