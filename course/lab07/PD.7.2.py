def insertion_sort(values,count):
    result=values[:]
    for index in range(1,len(result)):
        current=result[index]
        position=index
        while position > 0 and result[position-1]>current:
            count+=1
            result[position]=result[position-1]
            position-=1
        result[position]=current       
    return (result,count)

n=int(input())
arr=list(map(int,input().split()))
ordered_arr,count=insertion_sort(arr,0)

print(*ordered_arr)
print(count)