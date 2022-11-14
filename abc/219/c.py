x = input()
d = dict()
print(d)
for i in range(26):
    nxt = chr(i + ord("a"))
    d[x[i]] = nxt

n = int(input())
a = []

for _ in range(n):
    s = input()#変換前の文字
    t = ""#変換後の文字
    for char in s:
        t += d[char]
    a.append((t, s))
print(a)
a.sort()#変換後でソート
for i in range(n):
    print(a[i][1])