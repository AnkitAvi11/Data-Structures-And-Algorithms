n = int(input())

decimal = 0
i=0
while n!=0 : 
    remainder = n%10 
    decimal += pow(2,i)*remainder
    i+=1
    n//=10

print(decimal)