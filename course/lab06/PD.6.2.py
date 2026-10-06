class Book:
    def __init__(self,number):
        self.number=number
        self.use=False
        
    def status(self):
        return self.use
    
    def return_book(self):
        if self.use==True:
            self.use=False
            return True
        else:
            return False
        
    def borrow(self):
        if self.use==True:
            return False
        else:
            self.use=True
            return True


n=int(input())
num=list(map(int,input().split()))
q=int(input())

lib={}

for number in num:
    lib[number]=Book(number)

for _ in range(q):
    ask, number = input().split()
    number=int(number)
    book=lib[number]
    
    if ask=='STATUS':
        print("BORROWED" if book.status() else "AVAILABLE")
        
    elif ask=='RETURN':
        print("OK" if book.return_book() else "NOT_BORROWED")        
    
    else:
        print("OK" if book.borrow() else "ALREADY")