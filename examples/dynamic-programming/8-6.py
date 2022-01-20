# 개미 전사

n=int(input()) # 식량 창고 수
k=list(map(int, input().split())) # 각 식량 창고에 저장된 식량의 개수

d=[0]*100
d[0]=k[0]
d[1]=max(k[0],k[1])

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+k[i])

print(d[n-1])