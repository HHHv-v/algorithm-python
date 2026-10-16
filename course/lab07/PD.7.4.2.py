from bisect import bisect_left

n=int(input())
arr=list(map(int,input().split()))

for _ in range(int(input())):
    operation, raw_value=input().split()
    value=int(raw_value)
    position=bisect_left(arr,value)
    
    if operation=="ADD":
        arr.insert(position,value)
        print(position+1)
    elif position<len(arr) and arr[position]==value:
        print(position+1)
        if operation=="REMOVE":
            arr.pop(position)
    else:
        print(-1)