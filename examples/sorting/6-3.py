# 삽입 정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 첫번째 원소 7은 정렬된 것으로 판단
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j] # swap
        else: # 자신보다 작은 데이터를 만나면 멈춤
            break

print(array)
