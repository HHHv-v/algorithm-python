from bisect import bisect_left, bisect_right

n,q=map(int,input().split())
values=sorted(map(int,input().split()))

for _ in range(q):
    left,right=map(int,input().split())
    start=bisect_left(values,left)
    end=bisect_right(values,right)
    print(end-start)
    
    