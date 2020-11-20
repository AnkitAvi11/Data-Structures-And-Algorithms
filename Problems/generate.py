"""

Generate all the strings of length n drawn from 0 ... k -1

"""

def get_substring(string, counter, result, level, k) : 
    if level == k : 
        print(result)

    else : 

        for i in range(len(string)) : 
            if counter[i] == 1 : 
                result[level] = string[i]
                counter[i] = 0
                get_substring(string, counter, result, level+1, k)
                counter[i] = 1


if __name__ == '__main__' : 
    string = "abcdefgh"
    counter = [1 for _ in range(len(string))] 
    result = [0 for _ in range(len(string))]
    get_substring(string, counter, result,0, 4)