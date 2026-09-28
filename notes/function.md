# 04 함수

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
`sorted`가 필요할 때 대신 불러 쓰라고 함수 자체를 건네는 것이다.

<br>

### lambda가 필요한 경우

`len`처럼 이미 있는 함수로 표현할 수 없는 기준도 있다.
"두 번째 글자로 비교해" 같은 경우다. 이럴 때는 함수를 직접 만들어야 한다.

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

<br>

### 기준이 여러 개일 때

**튜플**로 넘긴다. 앞쪽 기준이 우선이고, 같으면 뒤쪽 기준으로 비교한다.

```python
# 두 번째 글자 기준, 같으면 단어 전체 사전순
sorted(words, key=lambda x: (x[1], x))
```

<br>

### sort()도 동일

`sort()` 메서드도 똑같이 `key`를 받는다. `reverse=True`와 함께 쓸 수도 있다.

```python
words.sort(key=lambda x: x[1])
sorted(words, key=len, reverse=True)
```
