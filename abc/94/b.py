n, m, x = map(int, input().split())
a = list(map(int, input().split()))


count_0 = 0
count_n = 0

n_list = list(range(n+1))
o_list = sorted(n_list, reverse=True)

for i in n_list[x+1:n+1]:
    if i in a:
        count_n +=1
        
for i in o_list[n-x-1:n+1]:
    if i in a:
        count_0 +=1


if count_n < count_0:
    print(count_n)
else:
    print(count_0)