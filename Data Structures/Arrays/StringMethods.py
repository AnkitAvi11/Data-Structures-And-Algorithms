

#   function to determine if a string has all unique characters.
def isUnique(string) : 

    #   using brute force
    # for i in range(len(string)-1) : 
    #     for j in range(i+1, len(string)) : 
    #         if string[i] == string[j] : 
    #             return False

    #   using sorting (optimised solution)
    # string = list(string)
    # string.sort()
    
    # for i in range(len(string)-1) : 
    #     if string[i] == string[i+1] : 
    #         return False

    #   using hashtables
    string = string.upper()

    table = [0 for x in range(26)]

    for el in string : 
        if table[ord(el) - 65] == 1 : 
            return False
        else : 
            table[ord(el) - 65] = 1

    return True


if __name__ == '__main__' : 
    print(isUnique("abcdefghijklmnopqrstuvwxyza"))