# 07_DFS



#### 수도 코드

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

#### 파이썬 코드

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

