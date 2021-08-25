# 11_BFS(Breadth Frist Search)

#### BFS

- 그래프를 탐색하는 방법 크게 두 가지
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth Frist Search, BFS)
- BFS는 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 큐를 활용



#### 알고리즘

*말로도 해보고 수도코드 및 코드 구현도 해보기.*

- 구현1 

  ```python
  '''
  7 8
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
  7 8
  1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
  '''
  
  def bfs(s, V):
      q = []                          # 큐 생성
      visited = [0]*(V+1)             # visited 생성
      q.append(s)                     # 시작점 인큐
      visited[s] = 1                  # 시작점 visited 표시
      while q:                        # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
          t = q.pop(0)                # 디큐 (꺼내서)해서 t에 저장
          print(t)                    # t에 대한 처리
          for i in range(1, V+1):                     # t에 인접이고 미방문인 모든 i에 대해
              if adj[t][i] == 1 and visited[i] == 0:
                  q.append(i)                         # enqueue(i)
                  visited[i] = visited[t] + 1         # i visited로 표시
  
  V, E = map(int, input().split())
  edge = list(map(int, input().split()))
  adj = [[0]*(V+1) for _ in range(V+1)]         # 인접행렬
  adjList = [[] for _ in range(V+1)]
  
  for i in range(E):
      n1, n2 = edge[2*i], edge[2*i+1]
      adj[n1][n2] = 1
      adj[n2][n1] = 1                     # 방향이 없는 그래프
  
      adjList[n1].append(n2)
      adjList[n2].append(n1)
  
  bfs(1, V)
  #bfs2(1, V)
  ```

  - 단점: 큐의 사이즈를 예측하기 어렵다. 중복으로 큐에 들어갈 수 있기 때문.

- 구현2

  ```python
  def bfs2(s, V):
      q = []                          # 큐 생성
      visited = [0]*(V+1)             # visited 생성
      q.append(s)                     # 시작점 인큐
      visited[s] = 1                  # 시작점 visited 표시
      while q:                        # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
          t = q.pop(0)                # 디큐 (꺼내서)해서 t에 저장
          print(t)                    # t에 대한 처리
          for i in adjList[t]:                     # t에 인접이고 미방문인 모든 i에 대해
              if visited[i] == 0:
                  q.append(i)                         # enqueue(i)
                  visited[i] = visited[t] + 1         # i visited로 표시
  ```

- 구현3 (front ,rear 인덱스 활용)

  ```python
  '''
  7 8
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
  7 8
  1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
  '''
  
  def bfs(s, V):
      q = [0]*V           # 큐생성
      front = -1
      rear = -1
      visited = [0]*(V+1) # visited 생성
      rear += 1           # 시작점 인큐
      q[rear] = s
      visited[s] = 1      # 시작점 visited
      while front != rear:    # 큐가 비어있지 않으면
          front += 1          # 디큐해서 t에 저장
          t = q[front]
          print(t)
          for i in range(1, V+1):     #  t에 인접하고 미방문인 모든 i에 대해
              if adj[t][i] == 1 and visited[i] == 0:
                  rear += 1           # 인큐 i
                  q[rear] = i
                  visited[i] = visited[t] + 1     # i 방문표시
  
  V, E = map(int, input().split())
  edge = list(map(int, input().split()))
  adj = [[0]*(V+1) for _ in range(V+1)]         # 인접행렬
  adjList = [[] for _ in range(V+1)]
  
  for i in range(E):
      n1, n2 = edge[2*i], edge[2*i+1]
      adj[n1][n2] = 1
      adj[n2][n1] = 1                     # 방향이 없는 그래프
  
      adjList[n1].append(n2)
      adjList[n2].append(n1)
  
  bfs(1, V)         
  ```

  

