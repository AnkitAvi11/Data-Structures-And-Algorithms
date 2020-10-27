
#   program : string compression
"""
Implement a method to perform basic string compression using the counts of characters.

"""

def compressString(string : str) -> dict : 
    i = 0
    result = ""
    while i < len(string) : 
        count = 1
        try : 
            while string[i+1] == string[i] : 
                i+=1
                count+=1
        except :
            pass

        result += "{}{}".format(string[i], count)
        i+=1
        
    return result

if __name__ == '__main__' : 
    string = input("Enter a string : ")

    print(compressString(string))

    