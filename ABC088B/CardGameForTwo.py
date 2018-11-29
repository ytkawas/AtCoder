N = int(input()) #カードの枚数
cards = list(map(int,input().split()))

# 降順にソート
cards.sort()
cards.reverse()
Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += cards[i]
    else:
        Bob += cards[i]
print(Alice - Bob)
