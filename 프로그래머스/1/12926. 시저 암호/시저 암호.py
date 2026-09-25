def solution(s, n):
    answer=[]
    
    for c in s:
        if(c==" "):
            answer.append(" ")
        elif ord(c)<97:
            answer.append(chr((ord(c)-ord('A')+n)%26+ord('A')))
        else:
            answer.append(chr((ord(c)-ord('a')+n)%26+ord('a')))
            
    return "".join(answer)