def solution(s):
    s = s.split(" ")
    answer=[]
    
    for word in s:
        if word==" ":
            answer.append(" ")
        else:
            for i in range(len(word)):
                word=list(word)
                if i%2==0:
                    word[i]=word[i].upper()
                else:
                    word[i]=word[i].lower()
                    
            answer.append("".join(word)) 
            
    return " ".join(answer)