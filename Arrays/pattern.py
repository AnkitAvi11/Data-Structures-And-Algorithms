#   program to pring a triangular pattern in python

def print_pattern(row : int) : 
    count = 1
    for i in range(1, row+1) : 
        for j in range(1, i+1) : 
            print(count, end = " ")
            count+=1

        print()


def pascal_triangle(row : int) : 
    
    pass


if __name__ == "__main__":
    print_pattern(5)