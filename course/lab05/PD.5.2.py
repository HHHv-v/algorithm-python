def count_digit(num,count=0):
    if num<10:
        return num,count
    return count_digit(sum_digit(num),count+1)
    
def sum_digit(num):
    if num<10:
        return 0
    return num%10+sum_digit(num//10)

n=int(input())

for _ in range(n):
    num=int(input())
    sum_num,count_num=count_digit(num)
    print(sum_num,count_num)