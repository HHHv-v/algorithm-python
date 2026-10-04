def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(f"{arr1[i] | arr2[i]:0{n}b}")
        answer[i]=answer[i].replace("1","#").replace("0"," ")
        
    return answer