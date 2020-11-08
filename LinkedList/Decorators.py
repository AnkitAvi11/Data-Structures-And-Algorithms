
def decoratorFunction(view_function) : 
    print("inside decorator")
    def wrapper_function(username) : 
        import re
        regex = re.compile('^([a-zA-Z0-9])+$')
        if re.match(regex, username) : 
            view_function(username)
        else : 
            print("Username entered is not valid")

    return wrapper_function


@decoratorFunction
def printFunction(username) : 
    print("Hello world from{}".format(username))

printFunction("ankit#")