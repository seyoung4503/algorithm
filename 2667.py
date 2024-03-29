import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    a = input()
    a = a[:-1]
    # print(a)
    data.append(list(map(int, a)))
# print(data)
visit = data[:]
ans = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# start = [x, y]
def bfs(start):
    q = deque()
    q.append(start)
    visit[start[0]][start[1]] = 0

    count = 0
    while len(q) > 0:
        now_x, now_y = q.popleft()
        count += 1
        # visit[now_x][now_y] = 0
        
        for i in range(4):
            next_node_x = now_x + dx[i]
            next_node_y = now_y + dy[i]

            if 0 <= next_node_x < n and 0<= next_node_y < n and visit[next_node_x][next_node_y] == 1:
                q.append([next_node_x, next_node_y])
                # count += 1
                visit[next_node_x][next_node_y] = 0
    
    return count

for i in range(n):
    for j in range(n):
        if visit[i][j] == 1:
            ans.append(bfs([i, j]))

print(len(ans))
ans.sort()
for i in ans:
    print(i)



