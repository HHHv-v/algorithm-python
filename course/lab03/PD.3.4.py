n=int(input())
arr1=list(map(int,input().split()))
arr2=[]
k=1

for i in range(n):
    if i != n-1 and arr1[i]==arr1[i+1]:
        k+=1
    else:
        arr2.append((arr1[i],k))
        k=1

print(len(arr2))
for x, y in arr2:
    print(x, y)