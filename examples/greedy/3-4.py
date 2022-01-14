import time
starttime=time.time()

n,k=map(int, input().split())

cnt=0
# while n>=k:
#     while n%k != 0:
#         n-=1
#         cnt+=1
#     n//=k
#     cnt+=1
# while n>1:
#     n-=1
#     cnt+=1

while True:
    if n<k:
        break

    # n이 k의 배수가 될 때까지 -1
    while n%k!=0:
        n-=1
        cnt+=1

    # n을 k로 나누기
    cnt+=1
    n//=k

cnt+=n-1
print(cnt)

endtime=time.time()
print(endtime-starttime)