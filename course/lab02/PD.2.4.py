n=int(input())
divisor_count=0
divisor_sum=0

for divisor in range(1,int(n**0.5)+1):
    if divisor**2==n:
        divisor_count+=1
        divisor_sum+=divisor
    
    elif n%divisor==0:
        divisor_count+=2
        divisor_sum=divisor_sum+divisor+(n//divisor)

print(divisor_count,divisor_sum)