# 럭키 스트레이트

n=int(input())
x=10

sum1=0
sum2=0
cnt=0

length=len(str(n))

while n>0:
    cnt+=1
    if cnt<=length/2:
        sum1+=n%x
    else:
        sum2+=n%x
    n//=x

if sum1==sum2:
    print("LUCKY")
else:
    print("READY")