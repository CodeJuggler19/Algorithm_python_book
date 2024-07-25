# from collections import deque

# 돌의 개수
n = int(input())

# 돌들의 정보
rocks = [0] + list(map(int, input().split()))

# 시작 지점
s = int(input())

v = [0 for i in range(n + 1)]

cnt = 1


def dfs(x):
    global cnt

    for i in range(2):
        len = rocks[x]
        if i == 0:
            move = x - len
        else:
            move = x + len

        if move < 1 or move > n:
            continue

        if v[move] == 0:
            v[move] = 1
            cnt += 1
            dfs(move)


dfs(s)
print(cnt)
