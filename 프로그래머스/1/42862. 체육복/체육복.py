def solution(n, lost, reserve):
    answer = 0
    clothes = [1]*(n+1)
    
    for i in lost: 
        clothes[i]-=1
    
    for i in reserve:
        clothes[i]+=1
    
    for i in range(1,n+1):
        if clothes[i]==0:
            if i-1>0 and clothes[i-1]==2:
                clothes[i]=1
                clothes[i-1]=1
            elif i+1<n+1 and clothes[i+1]==2:
                clothes[i]=1
                clothes[i+1]=1
                
    for i in range(1,n+1):            
        if clothes[i]>0:
            answer+=1
    
    return answer