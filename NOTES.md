# 파이썬 PS 노트

## 문법
- 리스트는 `-` 연산 불가. set은 가능하지만 중복이 제거됨
- `/`는 실수, `//`는 정수 나눗셈 (C와 다름)
- 증감 연산자(`++`, `--`) 없음 → `+=`, `-=` 사용
- 음수 인덱스: `lst[-1]` 마지막, `lst[-2]` 뒤에서 두 번째
- `or`는 단축 평가 — 앞이 참이면 뒤를 평가하지 않음

## 자료구조
| 개념 | C++ | Python |
| :--- | :--- | :--- |
| 동적 배열 | `vector` | `list` |
| 맵 | `unordered_map` | `dict` |
| 셋 | `unordered_set` | `set` |
| 큐 | `queue` | `collections.deque` |
| 우선순위 큐 | `priority_queue` | `heapq` |

## 자주 쓰는 함수
- `len(x)` — 길이
- `min()`, `max()`
- `dict.get(key, 기본값)` — 없으면 기본값 반환
- `deque.append()` / `.popleft()` / `.pop()` / `.appendleft()`

## 실수 기록
- 계산만 하고 대입 누락 (`count[name] - 1`)
- 함수 인자를 빈 값으로 덮어씀
- 비교 대상을 잘못 잡음 (큐 안 두 원소 vs 새 값)
- 문제를 잘못 읽음 (선택 방법 수 ≠ 종류 수)

## deque (큐 / 스택)

```python
from collections import deque
```

### 생성
| 코드 | 설명 |
| :--- | :--- |
| `q = deque()` | 빈 deque |
| `q = deque(arr)` | 리스트로 초기화 (원본은 변하지 않음) |
| `list(q)` | deque → 리스트 (반환 타입 맞출 때 필요) |

### 삽입 / 삭제
| 코드 | 설명 | C++ |
| :--- | :--- | :--- |
| `q.append(x)` | 뒤에 넣기 | `push_back` |
| `q.popleft()` | 앞에서 빼기 | `pop_front` |
| `q.appendleft(x)` | 앞에 넣기 | `push_front` |
| `q.pop()` | 뒤에서 빼기 | `pop_back` |
| `q.extend([a, b])` | 여러 개를 순서대로 추가 | |

- 큐로 쓸 때: `append` + `popleft`
- 스택으로 쓸 때: `append` + `pop`
- `append`는 한 번에 하나만. 리스트를 넣으면 리스트 자체가 원소 하나로 들어감 (`q.append([x, y])` → BFS 좌표 저장에 활용)

### 조회
| 코드 | 설명 |
| :--- | :--- |
| `q[0]` | 맨 앞 (빼지 않음) |
| `q[-1]` | 맨 뒤 |
| `q[-2]` | 뒤에서 두 번째 |
| `len(q)` | 크기 |
| `if q:` | 비어있지 않으면 참 |
| `if not q:` | 비어있으면 참 |

### 주의
- 리스트의 `pop(0)`은 O(N)이라 BFS에서 시간초과 발생. `deque.popleft()`는 O(1)
- 원소가 없는 상태에서 `q[-1]` 접근 시 IndexError
  → `if not q or q[-1] != x:` 처럼 단축 평가로 방어

### BFS 기본 골격
```python
q = deque([시작])
while q:
    cur = q.popleft()
    # 처리
    q.append(다음)
```
