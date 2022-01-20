# 반복적(bottom up-상향식) 피보나치 수열

d=[0]*100 # dp 테이블 - 결과 저장용

d[1]=1
d[2]=2
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])
