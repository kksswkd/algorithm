# 큰 수의 법칙

# n, m, k 입력받기
n, m, k = map(int, input().split())
# n개의 수 입력받기
data = list(map(int, input().split()))

# 입력받은 수 정렬
data.sort()
first = data[n-1] # 첫번째 큰 수
second = data[n-2] # 두번째 큰 수

result = 0
while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # 남은 횟수가 0이면 탈출
            break
        result += first
        m -= 1 # 횟수 -1
    if m == 0: # 남은 횟수가 0이면 탈출
        break
    result += second # 두번째로 큰 수 한번 더하기
    m -= 1 # 횟수 -1

print(result)