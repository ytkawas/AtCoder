A = int(input()) #500円玉の枚数
B = int(input()) #100円玉の枚数
C = int(input()) #50円玉の枚数
X = int(input()) #合計金額

result = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            sum = 500*a + 100*b + 50*c
            if sum == X:
                result += 1
                break
print(result)
