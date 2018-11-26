# 入力はs1s2s3の形式で与えられることを前提とする
marbles = int(input(),2)
result = 0
while marbles > 0:
    if marbles & 1:
        result += 1
    marbles >>= 1
print(result)
