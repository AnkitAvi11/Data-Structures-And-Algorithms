
from collections import Counter

def word_frequecy(words : str) : 

    counter = dict()

    for word in words : 
        if word in counter.keys() : 
            counter[word] += 1
        else : 
            counter[word] = 1  

    for key, value in counter.items() : 
        if value > 1 : 
            print("{} {}".format(key, value))
        else : 
            print(key)


if __name__ == '__main__' : 
    word_frequecy(["code", "while", "code"])