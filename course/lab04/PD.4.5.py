n=int(input())
market={}

# 입고 상품 정리
for _ in range(n):
    goods, count=input().split()
    market[goods]=market.get(goods,0)+int(count)
    
q=int(input())

# 상품 변동 시작
for _ in range(q):
    command=input().split()
    do=command[0]
    goods=command[1]
    
    if do=='COUNT':
        print(market.get(goods,0))
        
    elif do=='SELL':
        count=int(command[2])
        market[goods]=market.get(goods,0)-count
        if market[goods]==0:
            del market[goods]
            
    elif do=='ADD':
        count=int(command[2])
        market[goods]=market.get(goods,0)+count
    
    

d=len(market)
s=sum(market.values())    
print(f"TOTAL {d} {s}")