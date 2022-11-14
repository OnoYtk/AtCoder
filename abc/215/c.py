import itertools
s, k = input().split()
k = int(k)
s = sorted(list(s))
ans = set()

for i in itertools.permutations(s):
    word = ''.join(i)
    ans.add(word)
print(ans)
ans = sorted(list(ans))
print(ans[k-1])
