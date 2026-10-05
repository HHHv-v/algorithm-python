n=int(input())
arr=[]

for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))

xs=[p[0] for p in arr]
ys=[p[1] for p in arr]
print(min(xs), min(ys), max(xs), max(ys))

