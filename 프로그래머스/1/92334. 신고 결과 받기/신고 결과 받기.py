def solution(id_list, report, k):
    
    report_result={} # 신고결과 집계점수
    reporter={} # 신고를 한 사람들
    check=set() # 중복방지 확인
    
    for user in report:
        sender, recipient =user.split()
        
        # 신고 점수 집계 (중복확인 후)
        if (sender,recipient) not in check:
            check.add((sender,recipient))
            report_result[recipient]=report_result.get(recipient,0)+1
            
            # 신고 받은 사람에 대한 신고자 리스트 작성
            if recipient not in reporter:
                reporter[recipient]=[]
            reporter[recipient].append(sender)

    # 이메일을 받은 횟수
    answer={user:0 for user in id_list} 
    
    for recipient in report_result:
        if report_result[recipient]>=k:
            for send in reporter[recipient]:
                answer[send]+=1
                          
    return list(answer.values())