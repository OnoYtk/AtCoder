n = int(input())
a = list(map(int, input().split()))
alice = 0
bob = 0
while len(a) > 0:
    alice += max(a)
    a.remove(max(a))
    if len(a) < 1:
        break
    bob += max(a)
    a.remove(max(a))


print(alice - bob)