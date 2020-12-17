#   program to reverse words (in-place algorithm)

#   function to reverse the words
def reverse_words(string) : 
    
    string.reverse()
    
    start_pos = 0

    for i in range(len(string)) : 
        if string[i] == ' ' : 
            reverse_chars(string, start_pos, i-1)
            start_pos=i+1

    reverse_chars(string, start_pos, len(string)-1)


#   helper function to reverse the characters of a string from a given index to a given index
def reverse_chars(string, start, end) : 
    while start <= end : 
        string[start], string[end] = string[end], string[start]

        start+=1
        end-=1


#   driver code
if __name__ == "__main__":
    string = ['c','a','k','e',' ','p','o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
    reverse_words(string)
    print("".join(string))