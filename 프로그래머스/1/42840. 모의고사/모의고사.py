def solution(answers):
    
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    o=[0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            o[0]+=1
        
        if answers[i] == second[i%len(second)]:
            o[1]+=1
            
        if answers[i] == third[i%len(third)]:
            o[2]+=1
    
    answer=[]
    max_score=0
    max_score=max(o)
            
    for i in range(len(o)):
        if max_score==o[i]:
            answer.append(i+1)
    
    return answer