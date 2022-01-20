# 떡볶이 떡 만들기 - 이진 탐색
n,m=map(int, input().split())
array=list(map(int, input().split()))

result=0
start=0
end=max(array)
while start<=end:
    sum=0
    mid=(start+end)//2
    for i in array:
        if i>mid: # 자르기 전 떡 길이가 절단 길이보다 큰 경우만!!
            sum+=i-mid

    if sum<m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)


