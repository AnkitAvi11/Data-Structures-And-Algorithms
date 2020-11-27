#   paranthesis matching using stack

def is_valid(string : str) -> bool : 
    stack = list()

    for el in string : 
        if el == '(' : 
            stack.append(el)
        elif el == ')' :
            stack.pop()

    if len(stack) > 0 : 
        return False
    else : 
        return True


if __name__ == '__main__' : 
    string = "(((a+b)*(c-d))"        

    print(is_valid(string))
        