def binary_search(values,target):
    low=0
    high=len(values)-1
    while low<=high:
        middle=(low+high)//2
        if values[middle]==target:
            return target
        elif middle>high:
            low=middle+1
        else:
            high=middle-1
    return -1

            
            