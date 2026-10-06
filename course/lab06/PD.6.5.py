class Park:
    RATES={"CAR":(1000,200,5000),
           "TRUCK":(1500,300,7500),
           "BUS":(2000,500,12000)}
    
    def __init__(self,type):
        self.type=type
        self.parking=False
        self.total_time=0
    
    def enter(self,enter_time):
        if self.parking:
            return False
        self.parking=True
        self.enter_time=enter_time
        return True
    
    def exit(self,exit_time):
        if not self.parking:
            return False
        self.parking=False
        self.exit_time=exit_time
        self.total_time=exit_time-self.enter_time
        return self.fee(self.total_time)
        
    def fee(self, duration):
        if duration<=60:
            return self.RATES[self.type][0]
        
        total=self.RATES[self.type][0]+(duration-60+29)//30*self.RATES[self.type][1]
        return min(self.RATES[self.type][2],total)


n=int(input())
park={}
for _ in range(n):
    number, type=input().split()
    park[number]=Park(type)
    
q=int(input())
commands=[input().split() for _ in range(q)]
total_fee=0

for operation, *operands in commands:
    if operation=="ENTER":
        vehicle=park[operands[0]]
        if not vehicle.enter(int(operands[1])):
            print("ALREADY")
        else:
            print("OK")
    
    elif operation=="EXIT":
        vehicle=park[operands[0]]
        fee=vehicle.exit(int(operands[1]))
        if not fee:
            print("NOT_PARKED")
        else:
            total_fee+=fee
            print(fee)
            

print("TOTAL",total_fee)