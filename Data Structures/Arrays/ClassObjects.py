

class MyClass : 

    #   class variable
    username = "default username" 

    def __init__(self, name, email) : 
        #   instance variable
        print("MyClass __init__ called")
        self.name = name
        self.email = email

    def __str__(self) : 
        return self.username

class SecondClass : 
    def __init__(self, name, email) : 
        print("Second class __init__ called")
        self.namelength = len(name)
        self.nameemail = len(email)


#   constructor calls in multiple inheritance in python
class DerivedClass(MyClass, SecondClass) : 

    def __init__(self, name, email, password) : 
        super().__init__(name, email)   #   calls only the first class passed to it
        SecondClass.__init__(self, name, email) #   used to call the second class
        print("Derived class constructor")
        self.__password = password

    def __str__(self) : 
        return self.name + " " + self.email + " " + self.__password + " " +str(self.namelength )+ " " + str(self.nameemail)


if __name__ == '__main__' : 
    ob = DerivedClass('ankit', 'ankitemail', 'mypassword')
    print(ob)


    