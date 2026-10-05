r,c=map(int,(input().split()))
matrix=[]

for _ in range(r):
    row=list(map(int,input().split()))
    matrix.append(row)

rotated=[]

for col in range(c):
    new_row=[]
    
    for row in range(r-1,-1,-1):
        new_row.append(matrix[row][col])
        
    rotated.append(new_row)

for row in rotated:
    for index in range(len(row)):
        if index>0:
            print(" ", end="")
        print(row[index],end="")    
    print()  

