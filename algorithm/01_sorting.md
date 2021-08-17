# 01. 정렬



## 버블 정렬 (Bubble Sort)

***인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 알고리즘***

#### 정렬 과정

- 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
- 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬

#### 시간 복잡도

- O(n^2)

#### 코드

``` python
def BubbleSort(arry):
    for i in range(len(arry)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```





## 카운팅 정렬 (Counting Sort)

***집합에 각 항목이 몇 개씩 있는지 세어서 정렬하는 알고리즘***

#### 제한 사항

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
- 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함

#### 시간 복잡도

- O(n + k) : n은 리스트의 길이, k는 정수의 최대값

#### 코드

```python
def Counting_Sort(A, B, k): # A는 입력배열, B는 정렬된 배열, C는 카운트 배열
    C = [0] * k
    for i in range(0, len(B)): # 각 정수를 카운팅
        C[A[i]] += 1
        
    for i in range(1, len(C)): # C리스트를 누적으로 바꿈
        C[i] += C[i-1]
    
    for i in range(len(B)-1, -1, -1): # 끝에서부터 탐색, stable sorting 위함
        B[C[A[i]-1]] = A[i]			# A[i]에 해당하는 수의 위치를 C에서 찾아서 B에 할당
        C[A[i]] -= -1				# C[A[i]]의 값을 줄이면 다음 A[i]는 한칸 앞쪽에 B에 할당
```





## 선택 정렬 (Selection Sort)



#### 시간 복잡도

- O(n^2)

#### 선택 정렬

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
```



## 퀵 정렬 (Quick Sort)



## 삽입 정렬 (Insertion Sort)



## 병합 정렬 (Merge Sort)

