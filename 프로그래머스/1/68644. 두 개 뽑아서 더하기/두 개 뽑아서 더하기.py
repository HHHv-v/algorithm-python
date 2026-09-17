def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    # answer= set(answer) 중복제거
    # answer= sorted(answer) 정렬 후 리스트 반환
    
    return sorted(set(answer))