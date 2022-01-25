# 08_백트래킹



## 미로 찾기

#### 테스트케이스

```
# 출발 0, 0 도착 7, 7
# 경로 있음, 경로 없음, 경로가 여러 개
3
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 1 0 0 0 0 0
1 1 1 1 1 1 1 0
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 0 1 1 1 1
1 0 1 0 1 1 1 1
1 0 0 0 0 0 0 0
1 0 1 1 1 1 1 0
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
```

#### 모든 칸 방문

```python
def f1(i, j, N):  # 모든 칸을 방문하는 탐색
    maze[i][j] = 1  # i, j 방문표시. (진입한 칸을 벽으로 변경)
    for di, dj in [(0,1), (1,0), (0,-1), (-1, 0)]: # 4방향 탐색
        ni, nj = i + di, j + dj
        # 탐색 방향이 통로이면
        if 0<=ni< N and 0<=nj< N and maze[ni][nj]==0: # and visited[ni][nj]==0
            f1(ni, nj, N)


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
f1(0, 0, N) # 탐색 시작 (0,0), 미로의 크기 N
print(maze[N-1][N-1])
```

#### 출구를 찾으면 중단

```python
def f2(i, j, N):  # 출구를 찾으면 중단
    if i==N-1 and j==N-1:   # 출구에 도착한 경우
        return 1
    else:
        maze[i][j] = 1  # i, j 방문표시. (진입한 칸을 벽으로 변경)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                if f2(ni, nj, N): # 출구를 찾고 리턴하면
                    return 1        # 입구까지 리턴(남겨둔 갈림길을 탐색하지 않음)
        return 0                # 탐색 방향에서 출국를 찾지 못한 경우

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
print(f2(0, 0, N))
```

#### 경로의 수

```python
def f3(i, j, N): # 입구-> 출구 경로의 개수
    global  cnt
    if i == N-1 and j == N-1:
        cnt += 1                # 경로에 도착한 횟수
        return
    else:
        maze[i][j] = 1  # 없으면 무한 루프의 위험
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                f3(ni, nj, N)
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
f3(0, 0, N)
print(cnt)
```

#### 최단 거리

```python
def f4(i, j, N, c):  # c 지나온 칸의 개수, 최단 거리 찾기...모든 경로를 탐색
    global minV
    if i == N-1 and j == N-1:
        if minV > c + 1:          # 기존 경로보다 도착지 포함 경로의 길이가 더 짧으면
            minV = c + 1            # C+1 출발,도착을 포함한 경로의 길이
        return
    else:
        maze[i][j] = 2  # 없으면 무한 루프의 위험
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                f4(ni, nj, N, c+1)
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
minV = N*N
f4(0, 0, N, 0)
if minV == N*N: # 경로가 없는 경우
    print(-1)
else:
    print(minV)
```



## 부분 집합의 합

```python
def f(i, N, K): # 합이 K인 부분집합을 출력
    global cnt1
    cnt1 += 1
    if i==N: # 부분집합 생성완료
        s = 0
        for j in range(N):
            if bit[j]==1:
                s += A[j]
        if s == K: # 합이 찾는 값이면
            print(bit, end= ' ')
            for j in range(N):
                if bit[j]==1:
                    print(A[j], end =' ')  # 부분 집합 출력
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)

def f2(i, N, K, S, RS):
    global cnt2
    cnt2 += 1
    if S==K:
        print(bit, end=' ')
        for j in range(N):
            if bit[j] == 1:
                print(A[j], end=' ')  # 부분 집합 출력
        print()
    elif i==N:
        return
    elif S > K:
        return
    elif S+RS < K:
        return
    else:
        bit[i] = 1
        f2(i + 1, N, K, S+A[i], RS-A[i])
        bit[i] = 0
        f2(i + 1, N, K, S, RS-A[i])

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*10
cnt1 = 0
f(0, 10, 10)
print(cnt1)
cnt2 = 0
f2(0, 10, 25, 0, sum(A))
print(cnt2)

```



## 순열

#### 순열 구하기

```python
def f(i, N): # P[i]의 값을 결정
    if i == N:  #
        print(P)
    else:
        for j in range(i, N): # P[i] <-> P[j] 자리교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]
        return

P = [1,2,3]
f(0, 3)
```

#### SWEA > Learn > Course > Programming Intermediate > Stack2 > 배열 최소합

```python
def back_tracking(i, N, s):
    global  min_sum
    if i == N:
        if s < min_sum:
            min_sum = s
    elif s > min_sum:       # 부분합이 이미 min_sum을 넘을 경우 종료
        return
    else:
        for j in range(i, N):                       # 순열 구하기
            P[i], P[j] = P[j], P[i]
            back_tracking(i+1, N, s+arr[i][P[i]])   # 부분합 더해서 재귀
            P[i], P[j] = P[j], P[i]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    min_sum = 9 * N
    P = list(range(10))         # 순열을 기록할 리스트
    back_tracking(0, N, 0)
 
    print(f'#{tc} {min_sum}')