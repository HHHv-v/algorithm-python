# 메서드와 내장 함수

## 호출 방식이 다르다

```python
a.method()     # 메서드 — 대상 뒤에 점을 찍고 호출
func(a)        # 내장 함수 — 괄호 안에 대상을 넣어 호출
```

`s.sorted()`처럼 섞어 쓰면 에러가 난다.
`sorted`는 내장 함수라 점을 찍고 부를 수 없다.

```python
"cab".sort()        # AttributeError — 문자열에는 sort 메서드가 없음
sorted("cab")       # ['a', 'b', 'c']
```

괄호를 빼면 호출되지 않고 함수 자체를 가리킨다.

```python
d.keys          # <built-in method keys of dict ...>  호출 안 됨
d.keys()        # dict_keys([...])
```

<br>

## 쓸 수 있는 대상이 다르다

**메서드**는 그 자료형에만 있다.

```python
[1, 2].append(3)     # 리스트 메서드
"abc".upper()        # 문자열 메서드
"abc".append(3)      # AttributeError — 문자열에는 없음
```

**내장 함수**는 어디에도 속하지 않아서 여러 자료형에 쓸 수 있다.
단, 그 함수가 처리할 수 있는 값이어야 한다.

```python
len("abc")           # 3
len([1, 2])          # 2
len({1, 2, 3})       # 3

len(5)               # TypeError — 정수는 길이가 없음
sum(["a", "b"])      # TypeError — 문자열은 더할 수 없음
```

<br>

## 원본이 바뀌는지는 가변/불변이 결정한다

**메서드라서 원본을 바꾸는 게 아니다.** 대상이 가변인지 불변인지가 기준이다.

```python
a = [3, 1, 2]
a.sort()             # 리스트는 가변 → 원본이 정렬됨, 반환값 None

s = "hi"
s.upper()            # 문자열은 불변 → 원본 그대로, 새 문자열 반환
s = s.upper()        # 받아야 쓸 수 있음
```

| 자료형                 | 가변/불변 | 메서드 동작            |
| ---------------------- | --------- | ---------------------- |
| 문자열, 튜플           | 불변      | 새 값 반환             |
| 리스트, 딕셔너리, 집합 | 가변      | 원본 변경, `None` 반환 |

내장 함수는 원본을 바꾸는 경우가 없다. 항상 결과를 받아야 한다.

<br>

## 대입이 필요한지 판단하기

```python
# 원본을 바꾸는 것 → 대입하지 않는다
a.sort()  a.append(x)  a.reverse()  d.clear()  s.add(x)

# 원본을 바꾸면서 값도 돌려주는 것 → 값이 필요할 때만 받는다
a.pop()  d.pop(key)

# 새 값을 만드는 것 → 반드시 받는다
sorted(a)  len(a)  s.upper()  s.replace(...)  d.get(k)  d.values()
```

<br>

## 자주 쓰는 내장 함수

```python
len(a)        # 길이
sum(a)        # 합
max(a)  min(a)
sorted(a)     # 정렬된 새 리스트
reversed(a)   # 역순 (list()로 감싸야 리스트)
abs(-3)       # 절댓값
round(3.7)    # 반올림

int(x)  str(x)  list(x)  set(x)  tuple(x)  dict(x)     # 자료형 변환
range(n)      # 정수 수열
ord('a')      # 97    문자 → 코드
chr(97)       # 'a'   코드 → 문자
```

아직 정리 안 한 것: `enumerate`, `zip`, `map`

<br>

## 자료형별 메서드 요약

| 자료형   | 대표 메서드                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| 문자열   | `split` `join` `replace` `strip` `upper` `lower` `find` `count` `startswith`  |
| 리스트   | `append` `extend` `insert` `remove` `pop` `sort` `reverse` `index` `count`    |
| 딕셔너리 | `get` `keys` `values` `items` `pop` `clear` `update`                          |
| 집합     | `add` `update` `remove` `discard` `clear` `union` `intersection` `difference` |

자세한 내용은 각 파일 참고 — string.md, list.md, dict-set.md
