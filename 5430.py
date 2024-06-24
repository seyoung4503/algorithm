import sys
input = sys.stdin.readline


T = int(input())

for i in range(T):
    opcode = list(input())
    opcode = opcode[:-1]

    # print("xxx", list(reversed(opcode)))

    n = int(input())

    arr = str(input())
    if n > 0:
        arr = arr[1:-2]
        arr = list(map(int, arr.split(",")))
    else:
        arr = []

    isError = False
    # print(arr)
    left = 0
    right = n-1
    isForward = True
    ptr = left

    for code in opcode:

        if code == "R":

            if isForward == True:
                isForward = False
                ptr = right
            else:
                isForward = True
                ptr = left
            
            
        if code == "D":
            if n == 0 or left > right:
                isError = True
            if isForward == True:
                left += 1
            elif isForward == False:
                right -= 1

        # if n > 0 and left > right:
        #     isError = True
    
    # print(left, right)


    if isError == False:
        print("[", end="")
        if isForward == True:
            for x in range(left, right+1):
                print(arr[x], end="")
                if right != x:
                    print(",", end="")

        elif isForward == False:
            for x in range(right, left-1, -1):
                print(arr[x], end="")
                if left != x:
                    print(",", end="")

        print("]")
    else:
        print("error")


    # for code in opcode:
        
    #     if code == "R":
    #         # arr = R_func(arr)
    #         # print(arr)
    #     elif code == "D":
    #         if n == 0 or len(arr) == 0:
    #             isError = True
    #             print("error")
    #         else:
    #             arr = D_func(arr)
    

        


    # print(n)
    # print(arr)


