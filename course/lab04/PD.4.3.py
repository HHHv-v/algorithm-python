n=int(input())
arr=input().split()
q=int(input())

count={}

for x in arr:
    count[x]=count.get(x,0)+1

for x in range(q):
    word =input()
    print(count.get(word,0))
