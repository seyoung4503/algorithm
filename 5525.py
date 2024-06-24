import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

S = input()
S = S.split("I")
if S[0] == 'O':
    S.pop(0)

# print(S)
S.pop()
# print(S)


count = 0
ans = 0
for i in S:
    if i == "O":
        count += 1
    else:
        count = 0
    if count == N:
        ans += 1
        count = N - 1

print(ans)