def decoded_length(text,index):
    total=0
    
    while index<len(text) and text[index]!=')':
        if text[index].isalpha():
            total+=1
            index+=1
        else:
            repeat=int(text[index])
            inner_length,closing=decoded_length(text,index+2)
            total+=repeat*inner_length
            index=closing+1
    
    return total, index

text=input().strip()
length,_=decoded_length(text,0)
print(length)
