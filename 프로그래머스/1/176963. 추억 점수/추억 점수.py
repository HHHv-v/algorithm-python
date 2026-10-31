def solution(name, yearning, photo):
    memory={}
    total=[]
    
    for person,score in zip (name,yearning):
        memory[person]=score
        
    
    for row in photo:
        total_row=0
        for col in row:
            total_row+=memory.get(col,0)
        total.append(total_row)
    
    return total
    
        
        
        