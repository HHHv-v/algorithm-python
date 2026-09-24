def solution(strings, n):
    
    answer = sorted(strings,key=lambda word:(word[n],word))
    return answer