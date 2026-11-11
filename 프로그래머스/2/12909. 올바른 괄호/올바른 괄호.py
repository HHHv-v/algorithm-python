# 파이썬은 스택 자료형이 없어서 list를 스택처럼 사용
def solution(s):
    stack=[]
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            # 2) ( 가 모자란 경우 F
            else:
                return False
    
    
    if not stack:
        return True
    else:
        # 3) ) 가 모자란 경우 F
        return False
        
    
    
    