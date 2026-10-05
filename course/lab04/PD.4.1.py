n=int(input())
arr=list(map(int,input().split()))
have=set()
order=[]

for num in arr:
    if num not in have:
        have.add(num)
        order.append(num)

print(len(order))
print(*order)