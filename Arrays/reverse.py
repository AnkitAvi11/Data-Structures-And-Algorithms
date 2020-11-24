#   leetcode problem solution of reverse string

def strip_string(string : str) -> str : 
    res = " "
    i=0
    while i < len(string) : 
        if string[i].isalpha() : 
            res+=string[i]
        elif string[i] == ' ' : 
            res += " "
            j = i
            while string[j] == ' ' : j+=1
            i = j-1
            
        i+=1

    return res



def reverse_string(string : str) -> str : 
    string = strip_string(string)
    string = string.split(" ")
    string.reverse()
    string = " ".join(string)

    return string


def reverse_from_end(string : str) -> str : 
    res = " "
    i = len(string) - 1

    while i >= 0 : 
        
        if string[i].isalpha() : 
            res += string[i]
        elif string[i] == " " : 
            res += " "
            j = i 
            while j>=0 and string[j] == ' ' : j-=1
            i = j+1          

        i-=1

    return res


if __name__ == '__main__' : 
    print(reverse_string("a good   example"))