
#input
survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]

#-----------------

score={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
test=[('R','T'),('C','F'),('J','M'),('A','N')]
result={}
mbti=[]

# 유형별 점수 매기기
for i in range(len(choices)):
    front=survey[i][0]
    back=survey[i][1]
        
    if choices[i]==4:
        continue
    elif choices[i]<4:
        result[front]=result.get(front,0)+score.get(choices[i])
    else:
        result[back]=result.get(back,0)+score.get(choices[i])
            

# 총 점수로 유형 판단하기
for a,b in test:
    front=result.get(a,0)
    back=result.get(b,0)
    if front==back:
        mbti.append(a)
    else:
        mbti.append(b) if front>back else mbti.append(b)
        
print(''.join(mbti))    