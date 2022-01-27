# 문자열 뒤집기

# 해설지 방법
data=input()
cnt0=0
cnt1=0
if data[0]=='0':
    cnt0+=1
elif data[0]=='1':
    cnt1+=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='1':
            cnt0+=1
        else:
            cnt1+=1

print(min(cnt0, cnt1))

# 내 방법
# s=str(input())
# tmp=int(s[0])
# cnt_zero,cnt_one=0,0
# if tmp==0:
#     cnt_zero+=1
# elif tmp==1:
#     cnt_one+=1
#
# for i in s[1:]:
#     if tmp!=int(i):
#        if int(i)==0:
#            cnt_zero+=1
#        elif int(i)==1:
#            cnt_one+=1
#     # tmp=int(i)
#     # print(cnt_zero, cnt_one, end='///')
#
# print(min(cnt_zero, cnt_one))