
#   forming words of length 'k'
def form_words(string, k) : 
    i = 0
    result = list()

    while i < len(string) :
        try : 
            result.append(string[i:i+k])
        except : 
            result.append(string[i:])
        i+=k

    return result


# driver code
if __name__ == "__main__":
    print(form_words('the quick brown fox jumps over the lazy dog', 10))