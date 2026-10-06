class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.entry_time = None
    
    # 이 메서드는 자식 클래스가 반드시 직접 만들어야 한다
    # raise : 일부러 오류를 발생시키는 키워드
    # NotImplementendError : 내장 오류 "아직 구현되지 않음"
    def rates(self):
        raise NotImplementedError
    
    def enter(self,time):
        if self.entry_time is not None:
            return "ALREADY"
        self.entry_time=time
        return "OK"
    
    def exit(self, time):
        if self.entry_time is None:
            return None
        
        duration = time - self.entry_time
        self.entry_time = None
        return self.fee(duration)
    
    def fee(self, duration):
        base_fee, unit_fee, maximum_fee=self.rates()

        if duration <= 60:
            return base_fee
        
        units = (duration-60+29) // 30
        return min(base_fee+units*unit_fee,maximum_fee)

class Car(Vehicle):
    def rates(self):
        return 1000,200,5000

class Truck(Vehicle):
    def rates(self):
        return 1500,300,7000

class Bus (Vehicle):
    def rates(self):
        return 2000,500,12000
    
vehicle_classes={
    "CAR":Car,
    "TRUCK":Truck,
    "BUS": Bus
}

n= int(input())
vehicles={}

for _ in range(n):
    vehicle_id, vehicle_type=input().split()
    vehicles[vehicle_id]=vehicle_classes[vehicle_type](vehicle_id)

q=int(input())
commands=[input().split() for _ in range(q)]
total=0

for operation, vehicle_id, raw_time in commands:
    vehicle = vehicles[vehicle_id]
    time = int(raw_time)
    
    if operation == "ENTER":
        print(vehicle.enter(time))
    else:
        fee=vehicle.exit(time)
        
        if fee is None:
            print("NOT_PARKED")
        else:
            print(fee)
            total+=fee
            
print("TOTAL",total)    