n=int(input())
arr=list(map(int,input().split()))
l,r=map(int,input().split())


arr[l:r+1]=arr[l:r+1][::-1]

for index in range(n):
    if index > 0:
        print(" ",end="")
    print(arr[index],end="")
print()
'''
reverse=arr[l:r+1]

for i in range(l,r+1):
    arr[i]=reverse.pop()
    
print(*arr)
'''