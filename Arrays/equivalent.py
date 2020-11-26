#   program to check if two strings are equivalent

def check_equivalent(string1 : str, string2 : str) -> bool : 
    string1 = "".join(string1);string2="".join(string2)
    print(string1,string2)
    if len(string1) != len(string2) : return False


if __name__ == "__main__":
    print(check_equivalent(['ab', 'c'], ['a', 'bc']))

    
