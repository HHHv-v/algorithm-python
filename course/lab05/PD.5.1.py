def limit (score,low,high):
    if score<low:
        return low
    elif score>high:
        return high
    else:
        return score
    

n=int(input())
score=list(map(int,input().split()))
low,high=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(limit(score[i],low,high))

print(*arr)
print(sum(arr))


