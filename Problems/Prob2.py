#   expression = 3n + 2

x = int(input())

count = 0;i=1

while True : 
    num = 3*i + 2
    i+=1

    if num%4 != 0 : 
        print(num, end = " ")
        count += 1

    if count == x : 
        break