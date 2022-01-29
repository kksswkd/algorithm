# 문자열 압축

s=str(input())
step= len(s) // 2
x=0

# def solution(s):
#     cnt = 0
#     tmp=' '
#     for i in range(0, len(s) - step + 1): #0~2
#         for j in range(i, len(s), step): # i=0 j=0,2,4 // i=1 j=1,3 // i=2 j=2,4 // i=3 j=3
#             print(s[j:j + step], ",", j, end='//')
#             # if tmp==s[j:j+result]:
#             #     cnt+=1
#             #     print("same"+", "+tmp)
#             # else:
#             #     print("diff")
#             #     break
#             # tmp = s[j:j + result]

def solution(s):
    answer=len(s)
    for step in range(1, len(s)//2+1): # 압축 단위 최대치 = len(s)//2+1
        compressed="" # 압축 문자열 저장용
        prev=s[0:step]
        cnt=1
        for j in range(step, len(s), step):
            if prev==s[j:j+step]: # 앞 문자열 이전 문자열과 비교
                cnt+=1
            else: # 다른 문자열이 나왔다면
                compressed+=str(cnt)+prev if cnt>=2 else prev
                prev=s[j:j+step]
                cnt=1
        # 남아 있는 문자열 처리
        compressed+=str(cnt)+prev if cnt>=2 else prev
        answer=min(answer,len(compressed))
    return answer
print(solution(s))