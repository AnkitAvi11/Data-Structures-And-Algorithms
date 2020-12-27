
def reverse(n) : 
    temp = 0
    while n!=0 : 
        temp = temp*10 + n%10
        n //= 10

    return temp        

n=int(input())
result = reverse(n)
print(result)

