class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    
    @property # getter: 메서드를 괄호 없이 속성처럼 읽게 한다.
    def score(self):
        # _ : 클래스 내부에서만 쓰는 값이니 바깥에서 직접 건드리지 말라
        return self._score
    #
    @score.setter # setter: score property의 setter
    def score(self,value):
        self._score=max(0,min(100,value))
    
                    

n=int(input())
students={}

for _ in range(n):
    name, score=input().split()
    students[name]=Student(name,int(score))
    
q=int(input())
commands=[input().split() for _ in range(q)]

for command in commands:
    student=students[command[1]]
    
    if command[0]=="SET":
        student.score=int(command[2])
    elif command[0]=="ADD":
        student.score+=int(command[2])
        
    print(student.score)
