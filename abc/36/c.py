import bisect
n = int(input())
a = [int(input()) for i in range(n)] #縦に入力
b = sorted(set(a))
for i in a:
    print(bisect.bisect_left(b,i))