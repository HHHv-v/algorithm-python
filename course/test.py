def selection_sort(values):
    result = values[:] # 원본 보호용 복사
    for start in range(len(result)-1):
        min=start
        for index in range(start+1,len(result)):
            if result[index] < result[min]:
                min=index
        result[start],result[min]=result[min],result[start]
        
    return result

print(selection_sort([7,4,9,2]))