n=int(input())
arr=list(map(int,input().split()))
q=int(input())

for _ in range(q):
    
    input_arr=input().split()
    num=int(input_arr[1])
    
    if input_arr[0]=='A':
        arr.append(num)

    elif input_arr[0]=='I':
        arr.insert(num,int(input_arr[2]))
    
    elif input_arr[0]=='D':
            arr.pop(num)
    
if not arr:
    print("EMPTY")
else:
    print(*arr)    
    