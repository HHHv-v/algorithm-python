n=int(input())
mart={}

# 상품 이름(a), 입고 수량(b)
for x in range(n):
    a,b=input().split()
    b=int(b)
    mart[a]=mart.get(a,0)+b
    
q=int(input())

# 명령어(a), 상품 이름(b), 수량(c)
for x in range(q):
    command=input().split()
    action=command[0]
    name=command[1]
    
    if action=="COUNT":
        print(mart.get(name,0))
        
    elif action=="SELL":
        mart[name]-=int(command[2])
        if(mart[name])==0:
            del mart[name]
            
    elif action=="ADD":
        mart[name]=mart.get(name,0)+int(command[2])

d=len(mart)
s=sum(mart.values())

print(f"TOTAL {d} {s}")