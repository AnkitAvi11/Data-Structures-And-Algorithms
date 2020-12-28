
n = int(input())
c = int(input())

csum = 0;prod = 1

if c == 1 : 
    for i in range(1, n+1) : 
        csum += i
    print(csum)
elif c == 2 : 
    for i in range(1, n+1) : 
        prod *= i
    print(prod)
else : 
    print(-1)