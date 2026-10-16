def lower_bound(values,target):
    low=0
    high=len(values)
    
    while low < high:
        middle = (low+high)//2
        if values[middle]<target:
            low=middle+1
        else:
            high=middle
            
    return low

n=int(input())
arr=list(map(int,input().split()))
q=int(input())
commends=[input().split() for _ in range(q)]
answers=[]

for commend in commends:
    ask=commend[0]
    num=int(commend[1])
    result=lower_bound(arr,num)
    
    if ask=="FIND":
        if result < len(arr) and arr[result]==num:
            answers.append(result+1)
        else:
            answers.append(-1)
    
    elif ask=="ADD":
        arr.insert(result,num)
        answers.append(result+1)
            
    else:
        if result < len(arr) and arr[result]==num:
            arr.pop(result)
            answers.append(result+1)
        else:
            answers.append(-1)

for answer in answers:
    print(answer)