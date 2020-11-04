
from collections import Counter

def perfectString(string) : 
    
    counter = Counter(string)
    string_len = len(string)
    each_char_length = string_len//len(counter)
    
    res = 0   

    for el in counter.keys() : 
        if not counter[el] == each_char_length : 
            res += abs(counter[el] // each_char_length)


    return res


if __name__ == '__main__' : 
    print(perfectString("xyyzxyxxy"))
