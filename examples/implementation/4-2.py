# 시각

h=int(input()) # 시간 입력받기

cnt=0 # 3이 하나 이상 포함된 시간의 수

for i in range(h+1): # 0~h
    for j in range(60): # 0~59
        for k in range(60): #0~59
            if '3' in str(i) + str(j) + str(k):
                print(str(i) + str(j) + str(k))
                cnt+=1

print(cnt)