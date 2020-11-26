
#   balance a string problem leetcode weekly challenge

def balance_string(string : str) -> int : 
    stack = list();count=0

    for char in string : 
        if char == 'a' : 
            if stack and stack[len(stack)-1] == 'b':
                count+=1
                stack.pop()
        else : 
            stack.append(char)

    return count

if __name__ == "__main__":
    string = "bbaaaaabb"
    print(balance_string(string))
        


        

