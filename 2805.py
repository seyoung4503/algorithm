import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tree_height = list(map(int, input().split()))

min_tree_height = min(tree_height)

minimum_height = 0
for i in tree_height:
    minimum_height += (i - min_tree_height)


# print(tree_height)
# print(minimum_height)

def totalLength(tree_length):
    total_length = 0
    for i in tree_height:
        if i - tree_length > 0:
            total_length += (i - tree_length)
    return total_length

def binarysearch(tree_array_data, m):
    # min_tree = min(tree_array_data)
    min_tree = 0
    max_tree = max(tree_array_data)

    ans = []
    while min_tree <= max_tree:
        avg_tree = (min_tree + max_tree)//2
        total_avg = totalLength(avg_tree)

        if total_avg >= m:
            ans.append([avg_tree, total_avg])
            min_tree = avg_tree +1
        
        elif total_avg < m:
            max_tree = avg_tree - 1

    return max(ans)

    
print(binarysearch(tree_height, m)[0])