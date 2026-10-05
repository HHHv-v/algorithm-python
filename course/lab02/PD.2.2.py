a,b,c=map(int,input().split())

if a+b<=c or b+c<=a or a+c<=b:
    print("Invalid")
else:
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")
