from collections import deque

def solution(arr):
    
    q=deque()
    
    for number in arr:
        if not q or q[-1]!=number: q.append(number)
    
    return list(q)