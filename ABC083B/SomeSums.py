def sumOfEachDigit(i):
    sum = 0
    while i > 0:
        sum += int(i % 10)
        i /= 10
    return sum

N,A,B = map(int, input().split())
ans = 0
for i in range(1,N+1):
    sum = sumOfEachDigit(i)
    if A <= sum <= B:
        ans += i
print(ans)
