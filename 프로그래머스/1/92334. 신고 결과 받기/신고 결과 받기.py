def solution(id_list, report, k):
    
    reporter={} # 신고를 한 사람들
    
    for user in set(report):
        sender,recipient=user.split()    
        # 신고 받은 사람에 대한 신고자 리스트 작성
        if recipient not in reporter:
            reporter[recipient]=[]
        reporter[recipient].append(sender)

    # 이메일을 받은 횟수
    answer={user:0 for user in id_list} 
    
    # k번 이상 신고를 받은 사람들의 신고자들에게 이메일 보내기
    for recipient in reporter:
        if len(reporter[recipient])>=k:
            for sender in reporter[recipient]:
                answer[sender]+=1
                          
    return list(answer.values())