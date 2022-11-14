x = input()
a = list(x)
ans = "Strong"
if int(a[0]) == int(a[1]) == int(a[2]) == int(a[3]):
    ans = "Weak"

if (int(a[0])+1)%10 == (int(a[1])) and (int(a[1])+1)%10 == (int(a[2])) and (int(a[2])+1)%10 == (int(a[3])):
    ans = "Weak"
print(ans)