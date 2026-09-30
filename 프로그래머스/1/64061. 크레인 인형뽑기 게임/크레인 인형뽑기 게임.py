def solution(board, moves):
    stack=[]
    answer=0
    
    for i in moves:
        for j in range(len(board)):
            pick=board[j][i-1]
            if pick!=0:
                if stack and stack[-1] == pick:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(pick)
                board[j][i-1]=0
                break
                
                
    return answer