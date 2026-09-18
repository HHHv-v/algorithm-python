📝 풀이

접근
participant를 딕셔너리로 카운팅하고, completion을 돌며 1씩 차감. 남은 값이 0보다 큰 이름이 답.

시간 복잡도
O(n)

막힌 지점
- `count.get(name, 0) + 1` 결과를 대입하지 않음.
- 차감도 동일하게 대입 누락.
- 동명이인 고려 없이 `count[name] == 1`로 판별.
- 개선: `-= 1` 표기, 조건 만족 시 즉시 return, answer 미정의 시 UnboundLocalError 가능.

다른 풀이
두 리스트를 정렬 후 순차 비교해 다른 지점 반환 — O(n log n).
collections.Counter로 두 딕셔너리를 빼면 남는 키가 답.

재풀이
- [x] 1차 2026.09.18
- [ ] 2차
