def solution(clothes):
    closet={}
    for name, kind in clothes:
        closet[kind]=closet.get(kind,1)+1
    
    total=1
    for count in closet.values():
        total*=count
        
    total-=1
    
    return total
        
        