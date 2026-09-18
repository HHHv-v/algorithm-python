def solution(participant, completion):
    count={}
    
    for name in participant:
        count[name]=count.get(name,0)+1
        
    for name in completion:
        count[name]-=1
        
    for name in count:    
        if count[name]>0:
            answer = name    
    
    return answer