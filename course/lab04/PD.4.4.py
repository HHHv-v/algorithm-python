n=int(input())
road=list(map(int,input().split()))
q=int(input())

path={}
for i in range(n-1):
    start=road[i]
    end=road[i+1]
    path[(start,end)]=path.get((start,end),0)+1

for _ in range(q):
    a,b=map(int,input().split())
    print(path.get((a,b),0))