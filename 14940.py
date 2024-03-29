import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
start = [0, 0]

mini_map = []
for i in range(n):
    line = list(map(int, input().split()))
    if max(line) == 2:
        start = [i, line.index(2)]
    mini_map.append(line)

print(mini_map)
print(start)

visited = []
for i in range(n):
    visited.append([0 for j in range(m)])

visited[start[0]][start[1]] = 1
dnode = deque()
dnode.append(start)

def dfs():
    present = dnode.popleft()
    pos_x = present[0]
    pos_y = present[1]

    for i in range(4):
        pos_x 



