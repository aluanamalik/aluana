n = int(input())

for x in range(n):
    if x % 3 == 0 or x % 4 == 0:
        print(x, end=" ")
