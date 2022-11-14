n = int(input())
a = list(map(int, input().split()))

b = [i for i in a if i % 2 == 0]

for i in b:
    if i % 3==0 or i % 5==0:
        pass
    else:
        print("DENIED")
        exit()
    
print("APPROVED")