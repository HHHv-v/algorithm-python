from bisect import bisect_left

n=int(input())
arr=list(map(int,input().split()))
q=int(input())

for i in range(q):
    key=int(input())
    result=bisect_left(arr,key)
    if result>=n or arr[result]!=key:
        print(-1)
        continue
    print(result+1)
