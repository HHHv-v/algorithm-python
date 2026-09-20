# 02-2 문자열 자료형

문자열은 **불변(immutable)**이다.
따라서 아래 모든 메서드는 원본을 바꾸지 않고 **새 문자열을 반환**한다.
결과를 쓰려면 반드시 변수에 대입해야 한다.

```python
a = "abc"
a[0] = "A"      # TypeError — 문자열은 직접 수정 불가
```

<br>

## 문자열 인덱싱

C언어 배열처럼 인덱스로 문자에 접근할 수 있다.

```python
a = "Life is too short, You need Python"
a[0]      # 'L'
a[12]     # 's'
```

파이썬은 음수 인덱스로 뒤에서부터 셀 수도 있다. `-1`이 마지막 문자다.

```python
a[-1]     # 'n'
a[-2]     # 'o'
```

<br>

## 문자열 슬라이싱

`a[시작:끝]` — **끝 번호에 해당하는 문자는 포함되지 않는다.**
인덱싱·슬라이싱은 리스트, 튜플에서도 동일하게 동작한다.

```python
a = "Life is too short, You need Python"

a[0:4]      # 'Life'        0,1,2,3만 포함
a[12:17]    # 'short'       0부터 시작할 필요 없음
a[:17]      # 'Life is too short'          시작 생략 → 처음부터
a[19:]      # 'You need Python'            끝 생략 → 끝까지
a[:]        # 전체
a[19:-7]    # 'You need'    -7 바로 앞까지
```

콜론 한쪽을 비우면 그 방향의 끝을 의미한다. `0`을 넣는 게 아니다.

슬라이싱은 **값을 꺼내기만** 한다. 치환하지 않는다.
앞부분을 다른 문자로 바꾸려면 새로 조립해야 한다.

```python
s = "01033334444"
"*" * (len(s) - 4) + s[-4:]     # '*******4444'
```

<br>

## f 문자열 포맷팅

C처럼 `%` 방식도 쓸 수 있지만, 현재 주력은 f-string이다.
따옴표 **앞**에 `f`를 붙이고, 중괄호 안에 변수나 식을 넣는다.

```python
name = "홍길동"
age = 30
print(f"이름은 {name}이고, 나이는 {age}입니다.")
print(f"{age} + 5 = {age + 5}")     # 식도 가능

y = 3.42134234
print(f"{y:.4f}")     # '3.4213'  소수점 자릿수 지정
```

<br>

## 문자열 메서드

> 점을 찍고 부르는 `a.upper()`는 **메서드**,
> 괄호에 넣는 `len(a)`는 **내장 함수**다. 호출 방식이 다르다.

**1) 개수 세기 — count**

```python
a = "hobby"
a.count("b")      # 2
```

**2) 위치 찾기 — find**

처음 나온 위치를 반환. 없으면 `-1`.

```python
a = "Python is the best choice"
a.find("b")       # 14
a.find("k")       # -1
```

**3) 위치 찾기 — index**

`find`와 같지만, 없으면 `ValueError` 발생.

**4) 문자열 합치기 — join**

리스트·튜플의 원소를 구분자로 이어 붙인다. 원소는 모두 문자열이어야 한다.

```python
",".join(["a", "b", "c"])     # 'a,b,c'
"".join(["a", "b", "c"])      # 'abc'
```

**5) 대소문자 변환 — upper, lower**

```python
a = "hi"
a.upper()     # 'HI'
a.lower()     # 'hi'
```

**6) 공백 제거 — strip**

```python
a = "  hi  "
a.lstrip()    # 'hi  '    왼쪽
a.rstrip()    # '  hi'    오른쪽
a.strip()     # 'hi'      양쪽

"xxhixx".strip("x")     # 'hi'    인자를 주면 그 문자를 제거
```

**7) 문자열 바꾸기 — replace**

`replace(찾을 문자열, 바꿀 문자열)` — 원본은 그대로이므로 재대입이 필요하다.

```python
a = "Life is too short"
a = a.replace("Life", "Your leg")
print(a)      # 'Your leg is too short'
```

**8) 문자열 나누기 — split**

구분자로 나눠 **리스트**로 반환한다.

```python
"Life is too short".split()     # ['Life', 'is', 'too', 'short']
"a:b:c:d".split(":")            # ['a', 'b', 'c', 'd']
```

주의: 인자 유무에 따라 동작이 다르다.

```python
s = "a  b"        # 공백 2칸
s.split()         # ['a', 'b']
s.split(" ")      # ['a', '', 'b']    빈 문자열이 생김
```

인자를 생략하면 연속된 공백을 하나로 묶고 앞뒤 공백도 제거한다.

**9) 문자 종류 확인 — isalpha, isdigit**

```python
"abc".isalpha()     # True
"123".isdigit()     # True
"a1".isalpha()      # False
```

**10) 시작/끝 확인 — startswith, endswith**

```python
s = "Life is too short"
s.startswith("Life")     # True
s.endswith("short")      # True
```
