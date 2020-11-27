
#   function to get each word in words
def conver_to_word(number) : 
    num_dict = {
        1 : "One",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        0 : "Zero"
    }

    return num_dict.get(number, "Invalid digit")


if __name__ == '__main__' : 
    number = int(input("Enter a number : "))
    temp = number
    res = list()
    while temp!=0 : 
        res.append(temp%10)
        temp //= 10 

    res.reverse()

    for num in res : 
        print(conver_to_word(num), end = " ")
