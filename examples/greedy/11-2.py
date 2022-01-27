# 곱하기 혹은 더하기

# 해설지 방법
data=input()

result=int(data[0])
for i in range(1, len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)

# 내 방법
# data=list(map(int,input()))
#
# result=data[0]
# tmp=data[0]
#
# for i in data[1:]:
#     if i==0 or i==1 or tmp==0:
#         result+=i
#     else:
#         result*=i
#     tmp=i
#
# print(result)