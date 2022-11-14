n = int(input())
ans = ""
rem = n

while rem:#条件書かないと，0以下のときらしいい
    if rem % 2 ==1:
        ans += "A"
        rem -= 1
    else:
        ans +="B"
        rem //=2
""" 
print(rem)#0 
"""
print(ans[::-1])