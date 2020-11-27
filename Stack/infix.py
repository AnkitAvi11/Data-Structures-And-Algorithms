
#   python program to convert infix to postfix using stack


#   function to get the priority of the characters in the stack
def priority(char) : 
    if char == '/' or char == '*' or char == '^' : 
        return 3
    elif char == '+' or char == '-' : 
        return 2
    else : 
        return 1


#   function get the last element in the stack
def peek(arr) : 
    return arr[len(arr)-1]


#   function to convert infix to postfix
def infix_to_postfix(string : str) -> str : 
    stack = list()

    for char in string : 
        
        if char.isalpha() : 
            print(char, end=" ")
        elif char == '(' : 
            stack.append(char)
        elif char == ')' : 
            temp = stack.pop() 
            while stack and temp != '(' : 
                print(temp, end=" ")
                temp = stack.pop()
        else : 
            while stack and priority(peek(stack)) > priority(char) : 
                print(stack.pop(), end = " ")

            stack.append(char)

    while stack : 
        print(stack.pop(), end=" ")

if __name__ == "__main__":
    infix_to_postfix("a+(b/d)*e/(f*h)")

