# 두 배열의 원소 교체
n,k=map(int, input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse=True) # 내림차순 정렬

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

print(sum(a))
