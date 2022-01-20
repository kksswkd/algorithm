# 부품 찾기 - 계수 정렬

n=int(input())
array=[0]*1000001

for i in input().split(): # array 데이터 중복 가능
    array[int(i)]+=1

m=int(input())
target=list(map(int,input().split()))

for i in target:
    if array[i]>=1:
        print('yes', end=' ')
    else:
        print('no', end=' ')