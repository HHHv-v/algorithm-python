n=int(input())
words=input().split()
q=int(input())
count={}

for word in words:
    count[word]=count.get(word,0)+1

for _ in range(q):
    word=input()
    print(count.get(word,0))
