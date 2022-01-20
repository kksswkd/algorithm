# 효율적인 화폐 구성

n,m=map(int,input().split())

d=[10001]*(m+1) # dp테이블 초기화
d[0]=0
array=[]
for i in range(n):
    array.append(int(input()))

# bottom up 다이나믹 프로그래밍
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[i], d[j-array[i]]+1)

if d[m]==10001:
    print(-1) # m원을 만드는 방법이 없는 경우
else:
    print(d[m])
