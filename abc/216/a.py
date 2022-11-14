a = str(input())
x,y =a.split(".")
if 0 <= int(y) <= 2:
    print(x+"-")
elif 3 <= int(y) <= 6:
    print(x)
else:
    print(x+"+")

""" 
x, y = map(int, input().split('.'))
if y <= 2:
    print(str(x) + '-')
elif y <= 6:
    print(x)
else:
    print(str(x) + '+')
"""