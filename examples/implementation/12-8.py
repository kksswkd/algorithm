# 문자열 재정렬

s=str(input())

data=[]
sum=0
for i in s:
    if 'A' <= i <= 'Z':
        data.append(i)
    elif 0<=int(i)<=9:
        sum+=int(i)

data.sort()
data.append(sum)

for i in data:
    print(i, end='')
