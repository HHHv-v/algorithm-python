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
