n=int(input())
students=[]

for i in range(n):
    name, score, time = input().split()
    students.append((name,int(score),int(time)))

ordered=sorted(students,key=lambda item:(-item[1],item[2],item[0]))
# sorted는 원본을 두고, 새로운 값을 줌

for name in ordered:
    print(name[0])
    
