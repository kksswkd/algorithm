# 볼링공 고르기
n,m=map(int, input().split())
data=list(map(int, input().split()))

# 해설지 방법
array=[0]*11 # 무게별 볼링공 개수 저장용
for i in data:
    array[i]+=1

result=0
for i in range(1, m+1):
    n-=array[i] # 자신과 무게가 같은 볼링공을 선택하는 경우 제외 (A가 선택할 수 있는 경우의 수)
    result+=array[i]*n # (B가 선택하는 경우의 수와 곱하기)

print(result)

# 내 방법
# # data.sort()
# cnt=0
#
# for i in range(0, len(data)):
#     for j in range(i+1, len(data)):
#         if data[i]!=data[j]:
#             cnt+=1
#
# print(cnt)