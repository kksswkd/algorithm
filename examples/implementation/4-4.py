# 게임 개발

n,m=map(int,input().split())

d=[[0]*m for _ in range(n)] # 방문한 위치 저장을 위한 맵 초기화

x,y,direction=map(int,input().split())
d[x][y]=1 # 현재 위치 방문 처리

array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

# 시뮬레이션 시작
cnt=1
turn_time=0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x,y=nx,ny
        cnt+=1
        turn_time=0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1
        if turn_time==4:
            nx=x-dx[direction]
            ny=y-dy[direction]
            # 뒤로 갈 수 있는 경우
            if array[nx][ny]==0:
                x,y=nx,ny
            # 뒤가 바다인 경우
            else:
                break
            turn_time=0

print(cnt)
