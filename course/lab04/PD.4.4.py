n=int(input())
arr=input().split()
q=int(input())

count={}
for x in range(n-1):
    count[(arr[x],arr[x+1])]=count.get((arr[x],arr[x+1]),0)+1
    
for x in range(q):
    a,b=input().split()
    print(count.get((a,b),0))