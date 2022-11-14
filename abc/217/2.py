a = input()
b = input()
c = input()

d = ["ABC", "ARC", "AGC", "AHC"]

if a in d:
    d.remove(a)
if b in d:
    d.remove(b)
if c in d:
    d.remove(c)        


print(*d)