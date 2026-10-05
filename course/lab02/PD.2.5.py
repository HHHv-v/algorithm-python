n=int(input())


for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end="")
        else:
            print(".",end="")
    print()

'''
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+"."*(n-2)+"*")
'''