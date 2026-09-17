# [level 1] 두 개 뽑아서 더하기 - 68644 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/68644) 

### 성능 요약

메모리: 11.1 MB, 시간: 0.14 ms

### 구분

코딩테스트 연습 > 월간 코드 챌린지 시즌1

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 09월 17일 13:55:39

### 문제 설명

<p>정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>numbers의 길이는 2 이상 100 이하입니다.

<ul>
<li>numbers의 모든 수는 0 이상 100 이하입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>[2,1,3,4,1]</code></td>
<td><code>[2,3,4,5,6,7]</code></td>
</tr>
<tr>
<td><code>[5,0,2,7]</code></td>
<td><code>[2,5,7,9,12]</code></td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>2 = 1 + 1 입니다. (1이 numbers에 두 개 있습니다.)</li>
<li>3 = 2 + 1 입니다.</li>
<li>4 = 1 + 3 입니다.</li>
<li>5 = 1 + 4 = 2 + 3 입니다.</li>
<li>6 = 2 + 4 입니다.</li>
<li>7 = 3 + 4 입니다.</li>
<li>따라서 <code>[2,3,4,5,6,7]</code> 을 return 해야 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>2 = 0 + 2 입니다.</li>
<li>5 = 5 + 0 입니다.</li>
<li>7 = 0 + 7 = 5 + 2 입니다.</li>
<li>9 = 2 + 7 입니다.</li>
<li>12 = 5 + 7 입니다.</li>
<li>따라서 <code>[2,5,7,9,12]</code> 를 return 해야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

> ## 📝 풀이

### 접근
두 수를 뽑는 모든 경우를 이중 반복문으로 순회하며 합을 리스트에 모은다.
중복 제거를 위해 매번 탐색하면 O(n³)이 되므로, 모두 모은 뒤 set으로 한 번에 제거하고 정렬한다.
안쪽 반복은 i+1부터 시작해 같은 쌍을 두 번 세지 않는다.

### 시간 복잡도
O(n²) — 쌍 순회 n(n-1)/2. 정렬 포함해도 n ≤ 100이라 여유롭다.

### 막힌 지점
1. `len(numbers-1)`로 씀. 길이에서 빼는 것이므로 `len(numbers)-1`이 맞다.
2. `for j=i+1 in range(...)` 형태로 씀. 시작값은 `range(시작, 끝)`의 인자로 넘긴다.
3. `sorted`를 메서드처럼 `answer.sorted()`로 호출함.
   `sorted(대상)`은 독립 함수로, 순회 가능한 객체를 받아 정렬된 새 리스트를 반환한다. 결과를 대입해야 한다.
   `.sort()`는 리스트 전용 메서드이고 제자리 정렬 후 None을 반환한다. set에는 쓸 수 없다.
4. 초기값을 쓰지 않는 변수까지 선언함. append로 채울 변수만 초기화가 필요하고, 대입으로 덮어쓸 변수는 불필요하다.

### 다른 풀이
`itertools.combinations(numbers, 2)`로 쌍을 만들면 이중 반복문 없이 처리 가능.

### 재풀이
- [ ] 1차
- [ ] 2차
