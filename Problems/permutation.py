#   string permutation

def string_permutation(string, counter, result, level) : 
    if level == len(string) : 
        print(result)

    else : 

        for i in range(len(string)) : 
            if counter[i] == 0 : 
                continue
            else : 
                result[level] = string[i]
                counter[i] = 0
                string_permutation(string, counter, result, level+1)
                counter[i] = 1


if __name__ == "__main__":
    counter = [1,1,1]
    result = [0,0,0]
    string_permutation(['1', '2', '3'], counter, result, 0)