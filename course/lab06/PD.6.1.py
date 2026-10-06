class Reactangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def a(self):
        return self.width*self.height
    
    def b(self):
        return (self.width+self.height)*2

n=int(input())
arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    reactangle=Reactangle(a,b)
    arr.append((reactangle.a(),reactangle.b()))

for a,b in arr:
    print(a, b)
    
area=[i[0] for i in arr]

m=max(area)
print(f"MAX {area.index(m)+1} {m}")
