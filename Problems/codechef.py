
"""
Bytelandian gold problem solution in python

"""


def count_bytelandian_amoun(amount : int) -> int : 
    temp = amount
    count = 0 

    for i in range(2,5) : 
        count += temp//i

    return count


if __name__ == "__main__":
    print(count_bytelandian_amoun(12))

