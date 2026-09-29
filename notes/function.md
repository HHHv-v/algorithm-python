# 04 함수

## 함수 정의와 호출

```python
def 함수이름(매개변수1, 매개변수2, ...):
    실행할 코드
    return 반환값
```

정의만으로는 본문이 실행되지 않는다. 호출할 때마다 본문이 새로 실행된다.

```python
def greet():
    print("Hello")

greet()      # Hello
```

C와 다른 점은 반환형과 매개변수 타입을 적지 않고,
중괄호 대신 콜론과 들여쓰기로 블록을 구분한다는 것이다.

<br>

## 매개변수와 인자

- **매개변수(parameter)** — 정의할 때 쓰는 이름
- **인자(argument)** — 호출할 때 넘기는 값

```python
def greet(name):        # name이 매개변수
    print("Hello,", name)

greet("Mina")           # "Mina"가 인자
```

### 위치 인자

왼쪽부터 순서대로 대응된다. 순서가 바뀌면 의미가 달라진다.

```python
def subtract(left, right):
    return left - right

subtract(10, 3)     # 7
subtract(3, 10)     # -7
```

### 키워드 인자

이름으로 지정하므로 순서와 무관하다.

```python
def describe(name, score):
    print(name, score)

describe(score=92, name="Mina")     # Mina 92
```

### 기본값

호출할 때 생략하면 기본값이 쓰인다.

```python
def greet(name, message="Hello,"):
    print(message, name)

greet("Mina")                # Hello, Mina
greet("Joon", "Welcome,")    # Welcome, Joon
```

기본값 없는 매개변수가 **앞에** 와야 한다.
호출할 때도 위치 인자가 키워드 인자보다 앞에 와야 하고,
같은 매개변수에 두 번 값을 줄 수 없다.

<br>

## return

`return`을 만나면 그 자리에서 함수가 끝나고 값을 돌려준다.

```python
def square(number):
    return number * number

result = square(6)      # 36
```

### 조기 반환

결과가 정해지면 바로 끝낸다. `return` 뒤의 문장은 실행되지 않는다.

```python
def classify(number):
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    return "positive"
```

### return이 없으면 None

```python
def announce(message):
    print(message)

result = announce("Ready")     # Ready 출력
print(result)                  # None
```

**출력과 반환은 다르다.** `print`는 화면에 보여줄 뿐이고,
값을 받아 쓰려면 `return`이 필요하다.

### 여러 값 반환 → 튜플

쉼표로 나열하면 튜플 하나로 묶여 반환된다.

```python
def bounds(values):
    return min(values), max(values)

result = bounds([8, 3, 11, 5])       # (3, 11)  튜플
low, high = bounds([8, 3, 11, 5])    # 언패킹 — 개수가 맞아야 함
```

<br>

## 스코프 (변수 범위)

함수 안에서 만든 이름은 호출이 끝나면 사라진다.

```python
def calculate():
    subtotal = 12 + 8
    return subtotal

print(subtotal)     # NameError — 함수 밖에서는 없음
```

전역 변수는 **읽기만** 가능하다. 대입하면 같은 이름의 지역 변수가 새로 생긴다.

```python
count = 10

def show_count():
    count = 3        # 전역이 아니라 새 지역 변수
    print(count)     # 3

show_count()
print(count)         # 10 — 전역은 그대로
```

전역 변수에 대입하려면 `global` 선언이 필요하다.
다만 남용하면 함수를 이해하기 어려워지므로, 값을 인자로 넘기는 편이 낫다.

```python
count = 0

def increment():
    global count
    count += 1
```

<br>

## ★ 인자로 넘긴 객체는 복사되지 않는다

호출하면 매개변수가 **원본 객체를 그대로 가리킨다.**
그래서 가변인지 불변인지에 따라 결과가 달라진다.
(→ method-vs-function.md의 가변/불변 표)

### 불변 (정수, 문자열, 튜플)

함수 안에서 바꿔도 호출한 쪽은 그대로다.

```python
def increase(number):
    number += 1      # 새 정수를 가리킬 뿐

value = 5
increase(value)
print(value)         # 5
```

### 가변 (리스트, 딕셔너리, 집합)

함수 안에서 바꾸면 호출한 쪽도 바뀐다.

```python
def add_item(items, value):
    items.append(value)

numbers = [1, 2]
add_item(numbers, 3)
print(numbers)       # [1, 2, 3]
```

원본을 지키려면 복사한 뒤 바꾼다.

```python
def with_item(items, value):
    copied = items.copy()
    copied.append(value)
    return copied

original = [1, 2]
result = with_item(original, 3)
print(original)      # [1, 2]
print(result)        # [1, 2, 3]
```

<br>

## ★ 가변 기본값 함정

기본값 객체는 **정의할 때 한 번만** 만들어져 모든 호출이 공유한다.

```python
def collect(value, items=[]):     # 위험
    items.append(value)
    return items

collect(1)     # [1]
collect(2)     # [1, 2]  ← 이전 호출 결과가 남아 있음
```

호출마다 새 객체가 필요하면 `None`을 기본값으로 두고 안에서 만든다.

```python
def collect(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

collect(1)     # [1]
collect(2)     # [2]
```

<br>

## 함수도 객체다

함수 이름을 괄호 없이 쓰면 함수 자체를 가리킨다.

```python
def triple(number):
    return number * 3

operation = triple      # 괄호 없음 — 함수 객체
operation(4)            # 12  괄호를 붙이면 호출
```

그래서 함수를 인자로 넘길 수 있다.

```python
def apply_twice(operation, value):
    return operation(operation(value))

def add_three(number):
    return number + 3

apply_twice(add_three, 4)     # 10
```

`sorted(words, key=len)`에서 `len`을 괄호 없이 넘긴 것이 같은 원리다.

<br>

## lambda

함수를 만드는 예약어로, `def`와 같은 역할을 한다.
함수를 한 줄로 간결하게 만들 때 사용한다.

```python
lambda 매개변수1, 매개변수2, ... : 표현식
```

`return`이 없어도 표현식의 결괏값을 반환한다.

```python
add = lambda a, b: a + b
result = add(3, 4)
print(result)      # 7
```

다만 위처럼 변수에 담아 쓸 거면 `def`를 쓰는 편이 낫다.
`lambda`가 실제로 쓰이는 곳은 **정렬 기준 같은 것을 다른 함수에 알려줄 때**다.

<br>

## sorted에서 정렬 기준 지정 — key

`sorted`는 정렬하는 방법은 알지만 **무엇을 기준으로** 정렬할지는 모른다.
그걸 알려주는 것이 `key`다.

```python
words = ["banana", "kiwi", "apple"]

sorted(words)              # ['apple', 'banana', 'kiwi']  기준 없음 → 사전순
sorted(words, key=len)     # ['kiwi', 'apple', 'banana']  "길이로 비교해"
```

`key=len`은 "각 단어를 `len`에 넣어서 나온 값으로 비교하라"는 뜻이다.
`sorted`가 내부에서 `len("banana")`, `len("kiwi")`를 각각 불러
6, 4를 얻고 그 숫자로 정렬한다.

주의: `len(words)`처럼 호출하는 게 아니라 **괄호 없이 `len`만** 넘긴다.

### lambda가 필요한 경우

`len`처럼 이미 있는 함수로 표현할 수 없는 기준도 있다.
"두 번째 글자로 비교해" 같은 경우다.

```python
# 1. def로 만들어서 이름을 넘기기
def second(x):
    return x[1]

sorted(words, key=second)

# 2. lambda로 그 자리에서 쓰기
sorted(words, key=lambda x: x[1])
```

둘은 똑같이 동작한다.
두 줄짜리 함수를 이름까지 붙여 따로 만드는 대신,
쓰는 자리에 바로 적는 것이 `lambda`다.

`x`에는 요소가 하나씩 들어온다. 위 예에서는 "banana", "kiwi", "apple"이
차례로 들어가고, `x[1]`은 각각 'a', 'i', 'p'가 된다.

### 기준이 여러 개일 때

**튜플**로 넘긴다. 앞쪽 기준이 우선이고, 같으면 뒤쪽 기준으로 비교한다.

```python
# 두 번째 글자 기준, 같으면 단어 전체 사전순
sorted(words, key=lambda x: (x[1], x))
```

### sort()도 동일

```python
words.sort(key=lambda x: x[1])
sorted(words, key=len, reverse=True)
```

<br>
<br>

# 재귀 (Recursion)

함수가 자기 자신을 호출해 **더 작은 같은 문제**를 푼다.

**두 가지가 반드시 필요하다.**
- **기저 조건(base case)** — 더 이상 호출하지 않고 끝나는 경우
- **재귀 단계(recursive step)** — 기저 조건을 향해 작아지는 호출

```python
def factorial(number):
    if number == 0:        # 기저 조건
        return 1
    return number * factorial(number - 1)    # 재귀 단계
```

<br>

## 계산은 돌아오면서 일어난다

```
factorial(4) = 4 * factorial(3)
             = 4 * 3 * factorial(2)
             = 4 * 3 * 2 * factorial(1)
             = 4 * 3 * 2 * 1 * factorial(0)
             = 4 * 3 * 2 * 1 * 1
             = 24
```

호출은 큰 값에서 작은 값으로 들어가고, 반환은 작은 값에서 큰 값으로 나온다.
각 호출은 자기만의 **스택 프레임**(매개변수, 지역 변수, 돌아갈 위치)을 가진다.

```python
def trace(number):
    if number == 0:
        print("base")
    else:
        print("enter", number)
        trace(number - 1)
        print("leave", number)

trace(2)
# enter 2 / enter 1 / base / leave 1 / leave 2
```

<br>

## 대표 패턴

```python
# 자릿수 합 — 10으로 나누며 끝자리 제거
def digit_sum(number):
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)

# 회문 판별 — 양 끝을 비교하고 안쪽으로
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
```

**인덱스를 매개변수로 넘기면 슬라이싱 비용이 없다.**
`text[1:-1]`은 매번 새 문자열을 만들어 O(N²)가 되지만,
위치만 넘기면 그 비용이 사라진다.

```python
def is_palindrome(text, left, right):
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome(text, left + 1, right - 1)
```

<br>

## 메모이제이션

같은 값을 반복 계산하지 않도록 딕셔너리에 저장해 재사용한다.
없으면 호출 수가 지수적으로 늘어난다.

```python
def count_paths(number, cache):
    if number < 0:
        return 0
    if number in cache:           # 이미 계산했으면 꺼내 씀
        return cache[number]
    cache[number] = (count_paths(number - 1, cache)
                   + count_paths(number - 2, cache)
                   + count_paths(number - 3, cache))
    return cache[number]

cache = {0: 1}
```

<br>

## 재귀 vs 반복

| | 재귀 | 반복 |
| --- | --- | --- |
| 상태 저장 | 스택 프레임 | 루프 변수 |
| 종료 조건 | 기저 조건 | 조건식 |
| 진행 | 작아지는 인자 | 갱신되는 루프 상태 |
| 파이썬 제약 | 깊이 제한 (기본 약 1000) | 없음 |

깊이 제한 때문에 재귀가 깊어지는 문제는 `RecursionError`가 날 수 있다.
그럴 때는 반복문으로 바꾸거나 제한을 늘린다.
