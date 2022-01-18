# 퀵 정렬
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end: # 원소가 한개인 경우 종료
        return
    pivot=start # 피벗은 첫번째 원소
    left=start+1
    right=end
    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 왼쪽부터 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1 # 피벗보다 큰 데이터가 아닐 때마다 오른쪽으로 한칸씩 이동

        # 피벗보다 작은 데이터를 찾을 때까지 오른쪽부터 반복
        while right>start and array[right]>=array[pivot]:
            right-=1 # 피벗보다 작은 데이터가 아닐 때마다 왼쪽으로 한칸씩 이동

        # 엇갈린 경우 작은 데이터와 피벗을 swap
        if left>right:
            array[right],array[pivot]=array[pivot],array[right],
        # 엇갈리지 않은 경우 큰 데이터와 작은 데이터를 swap
        else:
            array[left],array[right]=array[right],array[left],

        # 분할 이후 왼쪽 부분과 오른쪽 부분을 각각 재정렬
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)