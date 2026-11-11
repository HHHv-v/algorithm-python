# heapq — 힙 (우선순위 큐)

리스트를 **최소 힙(min-heap)**처럼 다루게 해 주는 표준 라이브러리 모듈이다.
`collections`에 속한 게 아니라 별도 모듈이다. (`deque`, `Counter`, `defaultdict`가 `collections`에 있음)

```python
import heapq
```

- 힙 전용 자료형이 따로 있는 게 아니라, **일반 리스트**의 원소 순서를 힙 조건에 맞게 유지해 주는 함수들의 모음이다.
- `heap[0]`은 항상 **최솟값**이다.
- 리스트 전체가 정렬돼 있는 건 아니다. 확실히 아는 위치는 `heap[0]`뿐이다.
- C로 배열 기반 힙을 만들 때 직접 짜던 삽입(up-heap)과 삭제(down-heap)를 함수가 대신 해 준다.

<br>

## 주요 함수

| 함수 | 하는 일 | 시간 복잡도 | 반환값 |
| :--- | :--- | :--- | :--- |
| `heapq.heapify(lst)` | 기존 리스트를 힙으로 바꿈 (제자리 변경) | O(n) | `None` |
| `heapq.heappush(heap, x)` | 값 넣기 | O(log n) | `None` |
| `heapq.heappop(heap)` | 최솟값 꺼내기 (제거) | O(log n) | 꺼낸 값 |
| `heap[0]` | 최솟값 확인만 (제거 안 함) | O(1) | 최솟값 |
| `len(heap)` | 원소 개수 | O(1) | 정수 |

```python
import heapq

nums = [5, 1, 8, 3]
heapq.heapify(nums)        # nums 자체가 힙 순서로 바뀜
print(nums)                # [1, 3, 8, 5]  ← 정렬된 건 아님
print(nums[0])             # 1

heapq.heappush(nums, 2)
print(nums)                # [1, 2, 8, 5, 3]

x = heapq.heappop(nums)
print(x)                   # 1
print(nums)                # [2, 3, 8, 5]
```

빈 리스트에서 시작해 `heappush`만 써도 된다.

```python
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
print(heap[0])             # 1
```

`heappop`을 반복하면 작은 값부터 순서대로 나온다.

```python
heap = [5, 1, 8, 3]
heapq.heapify(heap)
while heap:
    print(heapq.heappop(heap), end=' ')   # 1 3 5 8
```

<br>

## 자주 하는 실수

**1. `heapify` 결과를 대입하기**

```python
nums = heapq.heapify(nums)   # ✗ nums가 None이 됨
heapq.heapify(nums)          # ○ 제자리 변경
```

`heapify`, `heappush`는 리스트를 직접 바꾸고 `None`을 반환한다. `list.sort()`와 같은 성질이다.

**2. 빈 힙에서 `heappop`**

```python
heap = []
heapq.heappop(heap)          # IndexError: index out of range
```

꺼내기 전에 `if heap:`이나 `len(heap)`으로 확인한다. `heap[0]`도 마찬가지다.

**3. 힙에 `append` / `sort` 쓰기**

```python
heap.append(0)               # ✗ 힙 순서가 깨짐 → heap[0]이 최솟값이 아닐 수 있음
heapq.heappush(heap, 0)      # ○
```

**4. `heap[1]`을 두 번째로 작은 값으로 착각**

`heap[1]`, `heap[2]`는 루트의 두 자식일 뿐이라, 둘 중 어느 쪽이 두 번째로 작은지는 정해져 있지 않다.

<br>

## 최대 힙

`heapq`는 최소 힙만 지원한다. 최대 힙이 필요하면 **부호를 뒤집어서** 넣고, 꺼낼 때 다시 뒤집는다.

```python
heap = []
for x in [5, 1, 8, 3]:
    heapq.heappush(heap, -x)

biggest = -heapq.heappop(heap)
print(biggest)               # 8
```

<br>

## 튜플 넣기 — 기준이 여러 개일 때

튜플은 **첫 번째 원소부터** 비교하고, 같으면 다음 원소를 비교한다.

```python
heap = []
heapq.heappush(heap, (3, 'c'))
heapq.heappush(heap, (1, 'b'))
heapq.heappush(heap, (1, 'a'))

print(heapq.heappop(heap))   # (1, 'a')
print(heapq.heappop(heap))   # (1, 'b')
print(heapq.heappop(heap))   # (3, 'c')
```

`(우선순위, 값)` 형태로 넣으면 우선순위가 작은 것부터 꺼낼 수 있다. (다익스트라에서 `(거리, 노드)`로 쓰는 형태)

<br>

## 참고: nsmallest / nlargest

```python
nums = [5, 1, 8, 3, 9]
heapq.nsmallest(2, nums)     # [1, 3]
heapq.nlargest(2, nums)      # [9, 8]
```

힙으로 바꾸지 않은 리스트에도 쓸 수 있다. 결과는 새 리스트로 반환된다.

<br>

## 정리

| 하고 싶은 것 | 쓰는 방법 |
| :--- | :--- |
| 리스트를 힙으로 | `heapq.heapify(lst)` |
| 넣기 | `heapq.heappush(heap, x)` |
| 최솟값 꺼내기 | `heapq.heappop(heap)` |
| 최솟값 보기만 | `heap[0]` |
| 비었는지 확인 | `if heap:` / `len(heap)` |
| 최대 힙 | `-x`로 넣고 `-heappop()` |
| 기준 여러 개 | 튜플 `(기준1, 기준2, ...)` |

> C++ `priority_queue`는 기본이 **최대** 힙이고, 파이썬 `heapq`는 **최소** 힙이다.
