
#   problem name : one away
"""
There are three types of edits that can be performed on trsings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away
"""

def oneAway(string, string2) : 

    if len(string) - len(string2) >= 2 : 
        return False

    count = 0
    for el in string : 
        if el not in string2 : 
            count+=1

    if count > 1 : 
        return False

    return True


if __name__ == '__main__' : 
    print(oneAway('pales', 'pale'))
