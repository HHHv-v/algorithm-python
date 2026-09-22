n,m=map(int,input().split())
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))

q1=len(s1 & s2)
q2=len(s1 - s2)
q3=len(s2 - s1)
q4=len(s1 | s2)

print(f"{q1} {q2} {q3} {q4}")

