# 02-5 딕셔너리 자료형

key와 value를 한 쌍으로 가지는 자료형이다.
딕셔너리는 **가변(mutable)**이라 추가·수정·삭제가 원본을 바로 바꾼다.
파이썬 3.7부터 삽입한 순서가 유지된다.

```python
{Key1: Value1, Key2: Value2, ...}

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
```

| key   | value         |
| ----- | ------------- |
| name  | pey           |
| phone | 010-9999-1234 |
| birth | 1118          |

value에는 어떤 자료형이든 올 수 있다.

```python
a = {'a': [1, 2, 3]}
```

빈 딕셔너리는 `{}`로 만든다. (빈 집합은 `set()` — `{}`는 딕셔너리로 해석됨)

<br>

## key로 value 얻기

```python
a = {1: 'a', 2: 'b'}
a[1]      # 'a'
a[2]      # 'b'
```

`a[1]`은 **인덱스 1이 아니라 key가 1인 값**을 의미한다.
딕셔너리는 위치(인덱스)로 접근할 수 없다.

없는 key로 접근하면 `KeyError`가 난다. → 안전하게 꺼내려면 `get` 사용

<br>

## 추가, 수정, 삭제

```python
a = {1: 'a'}

a[2] = 'b'            # 추가 — {1: 'a', 2: 'b'}
a['name'] = 'pey'     # 추가 — {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1, 2, 3]      # 추가 — {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

a[2] = 'z'            # 이미 있는 key면 수정 — {1: 'a', 2: 'z', ...}

del a[1]              # 삭제 — {2: 'z', 'name': 'pey', 3: [1, 2, 3]}
```

추가와 수정은 같은 문법이다. key가 없으면 추가, 있으면 덮어쓴다.

<br>

## key 규칙

**key는 중복될 수 없다.** 같은 key를 두 번 넣으면 마지막 값이 남는다.

```python
a = {1: 'a', 1: 'b'}
a         # {1: 'b'}
```

**key에는 불변 값만 쓸 수 있다.**
문자열, 숫자, 튜플은 가능하고 리스트는 불가능하다.

```python
a = {(1, 2): 'ok'}      # 튜플 key 가능
a = {[1, 2]: 'no'}      # TypeError — 리스트는 key 불가
```

<br>

## 딕셔너리 메서드

**1) key로 value 얻기 — get**

`a[key]`와 같지만, key가 없을 때 에러 대신 `None`이나 지정한 기본값을 반환한다.

```python
a = {'name': 'pey', 'phone': '010-9999-1234'}

a.get('name')              # 'pey'
a['nokey']                 # KeyError
a.get('nokey')             # None
a.get('nokey', '정보없음')  # '정보없음'
```

**★ 카운팅 패턴** — 코딩테스트에서 가장 많이 쓰는 형태

```python
count = {}
for x in ["a", "b", "a"]:
    count[x] = count.get(x, 0) + 1

count     # {'a': 2, 'b': 1}
```

- 처음 보는 key → `get`이 0을 반환 → 0 + 1 = 1 대입 (이때 key가 생김)
- 이미 있는 key → 기존 값 + 1
- **결과를 반드시 대입해야 한다.** `count.get(x, 0) + 1`만 쓰면 계산만 하고 버려진다.

**2) key 모음 — keys**

```python
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()           # dict_keys(['name', 'phone', 'birth'])
list(a.keys())     # ['name', 'phone', 'birth']
```

**3) value 모음 — values**

```python
a.values()         # dict_values(['pey', '010-9999-1234', '1118'])

scores = {'a': 90, 'b': 70}
sum(scores.values())    # 160
max(scores.values())    # 90
```

**4) key, value 쌍 — items**

`(key, value)` 튜플을 묶어서 반환한다.

```python
a.items()    # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ...])
```

`keys`, `values`, `items`는 리스트가 아니라 `dict_keys` 등의 객체를 반환한다.
for문에서는 그대로 쓰면 되고, 리스트가 필요하면 `list()`로 감싼다.

**★ for문에서 쓰는 형태**

```python
a = {'name': 'pey', 'birth': '1118'}

for k in a:                 # key만 — a.keys()와 같음
    print(k)

for v in a.values():        # value만
    print(v)

for k, v in a.items():      # 둘 다 — 튜플 다중 대입
    print(k, v)
```

**5) key 존재 여부 — in**

**value가 아니라 key를 검사한다.**

```python
a = {'name': 'pey', 'phone': '010-9999-1234'}
'name' in a      # True
'pey' in a       # False — 'pey'는 value라서
'email' in a     # False
```

**6) key로 꺼내기 — pop**

항목을 삭제하면서 value를 반환한다. 없는 key는 기본값을 지정할 수 있다.

```python
a = {'name': 'pey', 'phone': '010-9999-1234'}
phone = a.pop('phone')        # '010-9999-1234', a는 {'name': 'pey'}
email = a.pop('email', '없음') # '없음'
```

**7) 전부 지우기 — clear**

```python
a.clear()
a          # {}
```

<br>

## 자주 쓰는 내장 함수

```python
a = {'x': 3, 'y': 1}

len(a)                  # 2      key 개수
sorted(a)               # ['x', 'y']      key를 정렬한 리스트
sorted(a.items())       # [('x', 3), ('y', 1)]   key 기준 정렬
```

# 02-6 집합 자료형

중복을 허용하지 않고 순서가 없는 자료형이다.
집합은 **가변(mutable)**이라 `add`, `update`, `remove`, `discard`, `clear`는
**원본을 바꾸고 `None`을 반환**한다.

```python
s1 = set([1, 2, 3])     # {1, 2, 3}      리스트 → 집합
s2 = set("Hello")       # {'e', 'H', 'l', 'o'}   문자열 → 집합, 'l' 중복 제거
s3 = {1, 2, 3}          # {1, 2, 3}      중괄호로 바로 생성
s4 = set()              # 빈 집합 — {}는 딕셔너리가 되므로 주의
```

<br>

## 특징

**1) 중복을 허용하지 않는다.**
그래서 데이터의 중복을 제거하는 필터로 자주 쓴다.

**2) 순서가 없다.**
출력 순서가 넣은 순서와 다르고, 실행할 때마다 달라질 수도 있다.
인덱싱이 불가능하다.

```python
s = {1, 2, 3}
s[0]           # TypeError
```

순서가 필요하면 리스트로 바꾼다. 정렬된 결과가 필요하면 `sorted`를 쓴다.

```python
list(s)        # 리스트 — 순서는 보장 안 됨
sorted(s)      # 정렬된 리스트 — 항상 같은 순서
```

**3) 원소는 불변 값만 가능하다.** (딕셔너리 key와 같은 규칙)

```python
{(1, 2), 3}    # 튜플 가능
{[1, 2], 3}    # TypeError — 리스트 불가
```

<br>

## 포함 여부 — in

**코딩테스트에서 집합을 쓰는 가장 큰 이유다.**

```python
s = {1, 2, 3}
2 in s         # True
5 not in s     # True
```

|             | 리스트 `x in a`      | 집합 `x in s`    |
| ----------- | -------------------- | ---------------- |
| 방식        | 처음부터 끝까지 훑음 | 해시로 바로 찾음 |
| 시간 복잡도 | O(n)                 | 평균 O(1)        |

포함 여부를 여러 번 검사해야 하면 리스트를 집합으로 바꾸는 것만으로
시간 초과가 해결되는 경우가 많다.

<br>

## ★ 자주 쓰는 패턴

```python
nums = [3, 1, 2, 3, 1]

len(set(nums))       # 3           중복 제거 후 종류 수 — 폰켓몬
sorted(set(nums))    # [1, 2, 3]   중복 제거 후 오름차순 리스트 — 두 개 뽑아서 더하기
```

<br>

## 교집합 / 합집합 / 차집합

연산자와 메서드 두 방식이 있고 결과는 같다. **새 집합을 반환**하며 원본은 바뀌지 않는다.

```python
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

s1 & s2                 # {4, 5, 6}                     교집합
s1.intersection(s2)

s1 | s2                 # {1, 2, 3, 4, 5, 6, 7, 8, 9}   합집합
s1.union(s2)

s1 - s2                 # {1, 2, 3}                     차집합
s1.difference(s2)
s2 - s1                 # {7, 8, 9}
```

<br>

## 집합 메서드

모두 **원본을 바꾼다.**

**1) 값 1개 추가 — add**

```python
s = {1, 2, 3}
s.add(4)            # {1, 2, 3, 4}
s.add(2)            # {1, 2, 3, 4}   이미 있으면 변화 없음
```

**2) 여러 개 추가 — update**

```python
s = {1, 2, 3}
s.update([4, 5, 6])     # {1, 2, 3, 4, 5, 6}
```

**3) 제거 — remove / discard**

둘 다 값을 제거한다. 차이는 **없는 값을 제거할 때**다.

```python
s = {1, 2, 3}
s.remove(2)         # {1, 3}
s.remove(9)         # KeyError — 없는 값

s = {1, 2, 3}
s.discard(2)        # {1, 3}
s.discard(9)        # 에러 없음, 변화 없음
```

|           | 없는 값 제거 시     |
| --------- | ------------------- |
| `remove`  | `KeyError`          |
| `discard` | 아무 일도 안 일어남 |

**4) 전부 지우기 — clear**

```python
s = {1, 2, 3}
s.clear()
s                   # set()
```
