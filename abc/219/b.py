s1 = str(input())
s2 = str(input())
s3 = str(input())
t = str(input())

for i in range(len(t)):
    if t[i] == "1":
        print(s1,end="")
    elif t[i] == "2":
        print(s2,end="")
    elif t[i] == "3":
        print(s3,end="")
"""""
S1 = input()
S2 = input()
S3 = input()
T = input()
T = T.replace('1', S1)  # replaceはT自体が変化するのではなく、Tを変化したものを返すので、T = T.replace('1', S1) と書く必要があります
T = T.replace('2', S2)
T = T.replace('3', S3)
print(T)
"""