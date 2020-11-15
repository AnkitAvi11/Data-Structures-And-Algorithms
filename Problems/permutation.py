#   string permutation

def string_permutation(str, counter, result, level) : 
    if level == len(str) : 
        print(result)

    else : 
        for i in range(len(str)) : 
            if counter[i] == 1 : 
                result[level] = str[i]
                counter[i] = 0
                string_permutation(str, counter, result, level+1)
                counter[i] = 1
            else : 
                continue


if __name__ == "__main__":
    counter = [1,1,1]
    result = [0,0,0]
    string_permutation(['a', 'b', 'c'], counter, result, 0)