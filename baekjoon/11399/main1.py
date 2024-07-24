# ATM
n = int(input())

data = list(map(int, input().split()))

data.sort()

result = 0
before = 0

for i in range(n):
    before = before + data[i]
    result += before

print(result)


