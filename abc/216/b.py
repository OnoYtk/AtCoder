n = int(input())
s = list(input() for i in range(n))

if len(set(s)) < len(s):
    print("Yes")
else:
    print("No")