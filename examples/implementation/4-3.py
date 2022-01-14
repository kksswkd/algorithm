# 왕실의 나이트

input_data=input()
row=int(input_data[1])
col=int(ord(input_data[0]))-int(ord('a'))+1 # ord(문자) 유니코드 정수 반환 함수

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt=0
for step in steps:
    nrow=row+step[0]
    ncol=col+step[1]

    # 공간을 벗어나는 경우
    if nrow<1 or nrow>8 or ncol<1 or ncol>8:
        continue
    cnt+=1

print(cnt)