#   Word cloud data


#   function to split the string into words
def split_string(string : str) -> list :

    result = list();pos=0
    
    for index, value in enumerate(string) : 
        if not value.isalpha() : 
            result.append(string[pos:index])
            pos = index+1

    result.append(string[pos:])
    return result


#   function to count the words in dictionary
def word_cloud(string : str) -> dict : 
    count_dict = dict()

    splitted_string = split_string(string)

    for el in splitted_string : 
        if el in count_dict :
            count_dict[el] += 1
        else : 
            count_dict[el] = 1

    return count_dict
    


#   driver code
if __name__ == "__main__":
    print(split_string("ankit kumar"))
    print(word_cloud('ankit kumar singh ankit'))
