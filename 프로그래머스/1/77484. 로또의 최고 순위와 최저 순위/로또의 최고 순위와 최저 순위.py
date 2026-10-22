def solution(lottos, win_nums):
    zero=0
    collect=0
    
    # 1. 로또번호와 맞는 숫자의 개수와 0의 개수를 센다
    for lotto in lottos:
        # 번호가 알아볼수 없거나
        if lotto==0:
            zero+=1
        # 로또 번호와 일치하거나    
        elif lotto in win_nums:
            collect+=1
    
    # 2. 최고/최저 순위 번호를 찾는다
    match={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer=[match[zero+collect],match[collect]]
    
    return answer

        