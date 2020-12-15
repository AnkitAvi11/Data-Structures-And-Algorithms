def findPrefix(s, strings) : 
    result = list()
    
    for string in strings : 
        if s in string.lower() : 
            result.append(string)

    return result

if __name__ == "__main__":
    print(findPrefix('de', ['Dog', 'Dear', 'Deer']))