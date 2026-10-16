def lower_bound(values,target):
    low=0
    high=len(values)
    
    while low<=high:
        middle=(low+high)//2
        if values[middle]<target:
            low=middle+1
        else:
            high=middle
            
    return low

n=int(input())
values=(list(map(int,input().split())))
q=int(input())
targets=[int(input()) for _ in range(q)]
answers=[]

for target in targets:
    position=lower_bound(values,target)
    
    if position < n and values[position]==target:
        answers.append(str(position+1))
    else:
        answers.append("-1")

print("\n".join(answers))
