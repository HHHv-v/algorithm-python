n=int(input())
arr=list(map(int,input().split()))
    
print(len(set(arr)))

new_arr=[]
seen=set()

for x in arr:
    if x not in seen:
        seen.add(x)
        new_arr.append(x) 

print(*new_arr)
