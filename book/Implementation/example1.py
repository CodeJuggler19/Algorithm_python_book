n = input()

list = input().split()

x = 1
y = 1

for i in range(len(list)):
    if list[i] == 'R':
        if y != n:
            y += 1
    elif list[i] == "L":
        if y != 1:
            y -= 1
    elif list[i] == "U":
        if x != 1:
            x -= 1
    elif list[i] == "D":
        if x != n:
            x += 1
print(x, y)
