import sys
input = sys.stdin.readline

test = int(input())
for i in range(test):
    M, N, x, y = map(int, input().split())

    if M > N:
        s, t = N, M
        o, p = y, x
    else: 
        s, t = M, N
        o, p = x, y

    # print(s, t, o, p)

    not_in_first_cycle = True
    if x == y:
        print(x)
        not_in_first_cycle = False


    # x_y = (o + s) % t
    # count = (o + s) // t
    # while not_in_first_cycle:
    #     x_y = (x_y + s) % t
    #     if x_y == p:

    # print(x_y)
    # print(count)

    count = 1
    x_y = o + s
    while not_in_first_cycle:
        if x_y > t:
            x_y -= t

        # print(x_y)
        if x_y == p:
            print(count * s + o)
            break
        if x_y == o:
            print("-1")
            break
        count += 1
        x_y += s

# 10 12 7 2

# 1 1
# 2 2
# 3 3
# 4 4 
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
# 10 10
# 1 11
# 2 12
# 3 1
# 4 2
# 5 3
# 6 4
# 7 5
# 8 6
# 9 7
# 10 8
# 1 9
# 2 10
# 3 11
# 4 12
# 5 1
# 6 2
# 7 3
# 8 4 
# 9 5
# 10 6
# 1 7
# 2 8
# 3 9
# 4 10
# 5 11
# 6 12
# 7 1




# 5 4 4 4

# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
