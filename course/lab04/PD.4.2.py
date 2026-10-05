n1,n2=map(int,input().split())
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
result=[]
# 두 그룹에 모두 속한 구성원 수
result.append(len(s1&s2))
# 첫 번째 그룹에만 속한 구성원 수
result.append(len(s1-s2))
# 두 번째 그룹에만 속한 구성원 수
result.append(len(s2-s1))
# 두 그릅 중 하나 이상에 속한 전체 구성원 수
result.append(len(s1|s2))

print(*result)