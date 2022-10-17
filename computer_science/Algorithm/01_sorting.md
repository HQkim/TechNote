# 01. 정렬

## 버블 정렬 (Bubble Sort)

>  ***인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 알고리즘***

#### 정렬 과정

- 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
- 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬

#### 시간 복잡도

- O(N^2)

#### 코드

``` python
def bubble_sort(arry):
    for i in range(len(arry)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```



## 선택 정렬 (Selection Sort)

> ***현재 위치에 들어갈 값을 찾아 정렬하는 알고리즘***

#### 정렬 과정

1. 배열의 첫번째 인덱스부터 시작해서, 해당 인덱스를 포함해서 그 이후의 배열의 값들 중에서 가장 작은 값을 찾는다.

2. 가장 작은 값을 찾으면 해당 인덱스의 값과 바꿔준다.

3. 다음 인덱스에서 위 과정을 반복해준다.

#### 시간 복잡도

- O(N^2)

#### 코드

```python
def selection_sort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
```



## 삽입 정렬 (Insertion Sort)

> ***현재 위치에서 그 이하의 배열들을 비교하여 자신이 들어갈 위치를 찾아 그 위치에 삽입하는 알고리즘***

#### 정렬 과정

1. 두 번째 인덱스부터 시작해서, 비교 인덱스를 현재 인덱스 -1로 잡는다.
2. 현재 인덱스와 비교 인덱스의 배열 값을 비교한다.
3. 삽입 변수의 값이 더 작으면 현재 인덱스의 배열 값과 비교 인덱스의 배열 값을 서로 바꿔주고, 비교 인덱스를 -1하여 비교를 반복한다.
4. 만약 삽입 변수가 더 크면 다음 인덱스에서 위의 과정을 반복해준다.

#### 시간 복잡도

- 최악: O(N^2)

- 최선: O(N) (이미 정렬 되어 있는 경우)

#### 코드

```python
array = [8,4,6,2,9,1,3,7,5]

def insertion_sort(array):
    n = len(array)
    cnt = 0 
    for i in range(1, n):
        for j in range(i, 0, - 1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
        print(array[:i+1])
        
print("before: ",array)
insertion_sort(array)
print("after:", array)
```



## 카운팅 정렬 (Counting Sort)

> ***집합에 각 항목이 몇 개씩 있는지 세어서 정렬하는 알고리즘***

#### 제한 사항

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
- 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함

#### 시간 복잡도

- O(N + K) : N은 리스트의 길이, K는 정수의 최대값

#### 코드

```python
def counting_sort(A, B, k): # A는 입력배열, B는 정렬된 배열, C는 카운트 배열
    C = [0] * k
    for i in range(0, len(B)): # 각 정수를 카운팅
        C[A[i]] += 1
        
    for i in range(1, len(C)): # C리스트를 누적으로 바꿈
        C[i] += C[i-1]
    
    for i in range(len(B)-1, -1, -1): # 끝에서부터 탐색, stable sorting 위함
        B[C[A[i]-1]] = A[i]			# A[i]에 해당하는 수의 위치를 C에서 찾아서 B에 할당
        C[A[i]] -= -1				# C[A[i]]의 값을 줄이면 다음 A[i]는 한칸 앞쪽에 B에 할당
```



## 병합 정렬 (Merge Sort)

> ***분할 정복(Divdie and conquer) 방식으로 설계된 알고리즘***

#### 정렬 과정

**분할**

1. 배열의 길이가 1보다 크다면, 배열을 중간 인덱스를 기준으로 두 개의 배열로 나눈다. 중간보다 인덱스가 작은 배열을 A배열이라 하고, 중간보다 인덱스가 큰 배열을 B배열이라고 하자.

**병합**

2. A배열의 시작 인덱스를 i라 하고, B 배열의 시작 인덱스를 j라 하자(둘 다 처음에는 0)

3. A[i]와 B[j]를 비교해서 A[i]가 더 작으면 A[i]를 저장할 배열C에 추가해주고, i의 값을 증가시킨다. B[j]가 더 작으면 B[j]를 C배열에 추가해주고 j의 값을 증가시킨다. 이 과정을 i와 j가 A, B배열의 길이를 벗어나지 않을 때까지 반복한다.

4. 남은 A배열과 B배열의 원소들을 C배열의 뒤에 추가해준다.
5. 이를 재귀적으로 반복한다.

![img](01_sorting.assets/Merge-sort-example-300px.gif)

#### 시간 복잡도

- O(NlogN)

#### 코드

```python
array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
	if len(array) < 2:
		return array
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	print(merged_arr)
	return merged_arr

print("before: ",array)
array = merge_sort(array)
print("after:", array)
```



## 퀵 정렬 (Quick Sort)

> 분할 정복과 pivot을 사용하여 정렬을 수행하는 알고리즘.

#### 정렬 과정

1. 정렬할 배열(array)의 길이가 1 이하면 그대로 리턴한다.
2. pivot으로 잡을 배열의 값 하나를 정한다. 맨 앞이나 맨 뒤, 혹은 전체 배열 값 중 중간값이나 랜덤 값으로 정한다. 
3. 분할을 진행하기 전에, 비교를 진행하기 위해 가장 왼쪽 배열의 인덱스를 저장하는 left 변수(배열), 가장 오른쪽 배열의 인덱스를 저장한 right 변수(배열) 그리고 pivot point의 값과 같은 값들을 저장할 eqaul 변수(배열)를 만든다.
4. array를 순회하면서 pivot의 값보다 작은 값들은 left로 큰 값들은 right로 같은 값들은 eqaul에 넣어준다.
5. 그리고 재귀적으로 left, right에 대해서도 1-3의 과정을 한 후에 최종적으로 left, equl, right를 합친 배열을 리턴한다.

![img](01_sorting.assets/Quicksort-example.gif)

#### 시간 복잡도

- 최악: O(N^2)
- 최선: O(NlogN)

####  코드

```python
array = [8,4,6,2,5,1,3,7,9,9]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    eqaul = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            eqaul.append(num)
    
    return quick_sort(left) + eqaul + quick_sort(right)

print(f'정렬전: {array}')
print(f'정렬후: {quick_sort(array)}')
        
```



### 참고

[기본 정렬 알고리즘(Sorting Algorithm) 요약 정리](https://hsp1116.tistory.com/33)

[정렬 알고리즘 종류와 설명(파이썬 예제)](https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
