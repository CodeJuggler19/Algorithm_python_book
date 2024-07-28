# 바이러스
from collections import defaultdict, deque

n = int(input())

m = int(input())

graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def bfs(start):
    q = deque()
    q.append(start)

    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(1)
result = [i for i in visited if visited[i]]
print(len(result) - 1)
