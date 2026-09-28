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

### split() vs split(" ")

**`split()` — 연속된 공백을 하나로 본다**

공백이 몇 칸이든 한 덩어리로 취급해서 한 번만 자른다.
앞뒤 공백도 제거된다.

```python
"a  b".split()      # ['a', 'b']
" a b ".split()     # ['a', 'b']    앞뒤 공백 사라짐
```

**`split(" ")` — 공백 하나하나를 기준으로 자른다**

공백 1개마다 한 번씩 자른다. 자른 기준(공백)은 결과에 남지 않는다.
공백이 붙어 있으면 그 사이에 글자가 없으므로 **빈 문자열**이 생긴다.

```python
"a  b".split(" ")      # ['a', '', 'b']       공백 2칸 → 빈 문자열 1개
"a   b".split(" ")     # ['a', '', '', 'b']   공백 3칸 → 빈 문자열 2개
```

공백 n칸 → 조각 n+1개 → 빈 문자열 n-1개

<br>

**쉼표로 보면 같은 원리다**

```python
"a,b".split(",")     # ['a', 'b']
"a,,b".split(",")    # ['a', '', 'b']
```

구분자는 자르는 칼 역할만 하고 결과에서 사라진다.
`''`는 공백이 아니라 "이 조각에 글자가 없다"는 뜻이다.

```python
' '     # 공백 문자, 길이 1
''      # 아무것도 없음, 길이 0
```

<br>

**공백이 1칸뿐이면 둘은 같다**

```python
"a b".split()       # ['a', 'b']
"a b".split(" ")    # ['a', 'b']
```

차이가 나는 건 공백이 2칸 이상이거나 앞뒤에 공백이 있을 때다.

```python
" a b ".split()       # ['a', 'b']
" a b ".split(" ")    # ['', 'a', 'b', '']
```

<br>

**join으로 합칠 때 차이가 드러난다**

`join`은 요소 **사이**에만 구분자를 넣는다. (요소 개수 - 1 = 구분자 개수)

```python
" ".join(['a', '', 'b'])    # 'a  b'   요소 3개 → 사이 2군데 → 공백 2칸
" ".join(['a', 'b'])        # 'a b'    요소 2개 → 사이 1군데 → 공백 1칸
```

`'a' + ' ' + '' + ' ' + 'b'` 에서 가운데 `''`는 길이가 0이라
아무 글자도 더하지 않는다. 그래서 공백만 2칸 남는다.

`split(" ")`은 빈 문자열이 남아서 원래 공백 개수가 복원되고,
`split()`은 그 정보가 사라져 공백이 1칸으로 줄어든다.

**공백 개수를 유지해야 하는 문제에서는 `split(" ")`를 써야 한다.**
(예: 이상한 문자 만들기 — 공백이 2칸 이상 올 수 있음)

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
