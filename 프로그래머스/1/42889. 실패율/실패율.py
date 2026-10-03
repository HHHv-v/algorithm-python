def solution(N, stages):
    fail={}

    # 실패율 측정
    for stage in range(1,N+1):
        stage_clear=0
        stage_user=0
        for user in stages:
            if user == stage:
                stage_clear+=1
            if user >= stage:
                stage_user+=1
                
        if stage_user==0:
            fail[stage]=0
        
        else:
            fail[stage]=stage_clear/stage_user
        
    # 배열 내림차순 정리
    fail=sorted(fail,key=lambda k: fail[k],reverse=True)
    
    return fail