import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())


tomato_box = []
for i in range(n):
    sub_tomato_box = list(map(int, input().split()))

    tomato_box.append(sub_tomato_box)

print(tomato_box)

