"""
Write an efficient function that checks whether any permutation of an input string is a palindrome or not.
"""

def check_permutation_palindrome(string : str) -> bool : 
    
    has_seen = set()

    for char in string : 
        if char in has_seen : has_seen.remove(char)
        else : has_seen.add(char)

    return len(has_seen) <= 1
    

if __name__ == "__main__":
    print(check_permutation_palindrome('civil'))