N = int(input())
length = []
for i in range(1,int(N**0.5) + 1):
  if N % i == 0:
    length.append(max(len(str(i)) ,len(str(N//i))))
print(min(length))