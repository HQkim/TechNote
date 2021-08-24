# 07_DFS



#### 수도 코드 - 스택

```
visited[], stack[] 초기화
DFS(v)
	v 방문;
	visited[v] <- true;
	do {
		if (v의 인접 정점 중 방문 안한 w 찾기)
			push(v);
		while( w ) {
			w 방문;
			visited[w] <- true;
			push(w);
			v<-w;
			v의 인접 정점 중 방문 안한 w 찾기
		}
		v<-pop(stack);
	} while(v)
end DFS()
```

#### 파이썬 코드1 - 스택

```python
def dfs(s, v):
    visited = [0]*(v+1)
    stack = []
    visited[s] = 1
    i = s
    print(node[i])
    while i!=0:
        for w in range(1, v+1):
            if adj[i][w] == 1 and visited[w] == 0:         
                stack.append(i)
                i = w
                visited[w] = 1
                print(node[i])
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
                

```

#### 파이썬 코드 2 - 재귀함수 (SWEA 1219 길찾기)

``` python
def dfs_recurvise(v):
  	global ans
    if v == 99:			# (target)
        ans = 1
        return
    
    visited[v] = 1
    
    for w in adj_list[v]:
        if not visited[w]:
            dfs_recursive(w)

for _ in range(10):
    tc, N = list(map(int, input().split()))
    road = list(map(int, input().split()))
    
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2 * i]].append(road[2 * i +1])
    
    visited = [0] * 100
    ans = 0
    
    print(f'{} {}'.format(tc, ans))
```

