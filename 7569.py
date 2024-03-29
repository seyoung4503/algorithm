import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

data = []
for i in range(h):
    sub_data = []
    # line = []
    for j in range(n):
        sub_data.append(list(map(int, input().split())))

    data.append(sub_data)

    