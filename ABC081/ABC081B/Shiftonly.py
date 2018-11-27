def shiftonly(N,list):
    for x in range(N):
        if (list[x] % 2) != 0:
            return 0

    result = 1
    while True:
        finished = False
        for x in range(N):
            list[x] /= 2
            if (list[x] % 2) != 0:
                finished = True
                break
        if finished:
            break
        else:
            result += 1

    return result

# 個数(1≤N≤200)
N = int(input())
# 正の整数のリスト(0は含まない)
list = list(map(int,input().split()))

print(shiftonly(N,list))
