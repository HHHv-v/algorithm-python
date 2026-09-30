def solution(board, moves):
    stack=[]
    answer=0
    
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] !=0:
                if stack and stack[-1] == board[j][i-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[j][i-1])
                
                board[j][i-1]=0
                break
                
                
    return answer