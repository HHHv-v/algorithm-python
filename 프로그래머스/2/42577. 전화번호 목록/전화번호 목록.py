def solution(phone_book):
    prefix_set=set(phone_book)
    for num in phone_book:
        for k in range(1,len(num)):
            if num[:k] in prefix_set:
                return False
            
    return True