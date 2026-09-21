def solution(arr):
    answer=[]
    answer.append(arr[0]) # 처음 요소는 넣고 시작
    j=0
    for i in range(len(arr)):
        if  i+1<len(arr) and answer[j]!=arr[i+1] :
            answer.append(arr[i+1])
            j+=1
    
    return answer