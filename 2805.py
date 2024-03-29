import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tree_height = list(map(int, input().split()))

min_tree_height = min(tree_height)

minimum_height = 0
for i in tree_height:
    minimum_height += (i - min_tree_height)

print(n, m)
print(tree_height)
print(min_tree_height)
print(minimum_height)

if min_tree_height == m:
    print(min_tree_height)
elif min_tree_height > m:
    