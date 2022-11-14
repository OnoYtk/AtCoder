n = int(input())
ans = 0
if 10 > n:
    ans = n
elif n > 9 and 100 > n :
    ans  += 9
elif n > 99 and 1000 > n :
    ans = 9 + (-99) + n
elif n > 999 and 10000 > n :
    ans = 9 + (-99) + 999
elif n > 9999 and 100000 > n :
    ans = 9 + (-99) + 999 + (-9999) + n
elif n > 99999 and 1000000 > n :
    ans = 9 + (-99) + 999 + (-9999) + 99999
elif n > 999999 and 10000000 > n :
    ans = 9 + (-99) + 999 + (-9999) + 99999 + (-999999) + n
    
print(ans)


n=int(input())
ans=0
for i in range(1,n+1):
  j=len(str(i))
  if j%2==1:
    ans+=1
print(ans)