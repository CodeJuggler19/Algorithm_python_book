# 왕실의 나이트
n = input()

# ord 함수 테스트
row = int(n[1])
col = int(ord(n[0]) - int(ord('a'))) + 1
print(row, col)

# 모든 경우의 수
m = 8

# 틀린 답
# if n[0] == 'a' or n[0] == 'b' or n[0] == 'g' or n[0] == 'h':
#     m -= 2
#     if n[0] == 'a' or n[0] == 'h':
#         m -= 1
#
# if n[1] == '1' or n[1] == '2' or n[1] == '7' or n[1] == '8':
#     m -= 2
#     if n[1] == '1' or n[1] == '8':
#         m -= 1

list = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
x = 0
# ord함수 쓰면 이렇게 할 일 없음
if n[0] == 'a':
    x = 1
elif n[0] == 'b':
    x = 2
elif n[0] == 'c':
    x = 3
elif n[0] == 'd':
    x = 4
elif n[0] == 'e':
    x = 5
elif n[0] == 'f':
    x = 6
elif n[0] == 'g':
    x = 7
elif n[0] == 'f':
    x = 8
y = int(n[1])

for i in range(len(list)):
    x1 = x + list[i][0]
    y1 = y + list[i][1]
    if x1 <= 0 or y1 <= 0:
        m -= 1

print(m)
