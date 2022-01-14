# 큰 수의 법칙
# 3-2.py 복잡도 보완

n,m,k = map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

# 가장 큰 수가 더해지는 횟수
max_cnt=m//(k+1)*k
max_cnt+=m%(k+1)

# 두번째 큰 수가 더해지는 횟수
sec_cnt=m-max_cnt

result=first*max_cnt+second*sec_cnt
print(result)

