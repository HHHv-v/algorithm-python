def solution(s, n):
    answer=[]
    for a in s:
        if a==" ":
            answer.append(" ")
        elif ord(a) < 97:
            answer.append(chr((ord(a)+n-ord('A'))%26+ord('A')))
        else :
            answer.append(chr((ord(a)+n-ord('a'))%26+ord('a')))
            
    return "".join(answer)