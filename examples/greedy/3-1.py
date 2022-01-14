# 거스름돈

n = 1260 # 거스름돈
cnt = 0 # 동전 개수
coin_types = [500, 100, 50, 10] # 동전 종류

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)