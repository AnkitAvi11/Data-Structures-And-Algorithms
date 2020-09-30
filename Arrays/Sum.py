# class Solution : 

#     def __init__(self, username, email, roll) : 
#         self.username = username
#         self.email = email
#         self.roll = roll

#     def __str__(self) : 
#         return self.username


# class ExtendingClass(Solution) : 

#     def __init__(self, username, email, roll , password) : 
#         super().__init__(username, email, roll)

#     def __str__(self) : 
#         string = super().__str__()
#         return string

    
# if __name__ == '__main__' : 
#     ob = Solution('ankit', 'asd')

class MyIterator : 

    def __iter__(self) : 
        self.num = 0
        return self

    def __next__(self) : 
        if self.num == 10 : 
            print("List is done")
            raise StopIteration
        else : 
            self.num = self.num + 1
            return self.num

if __name__ == '__main__' : 
    ob = MyIterator()
    for i in ob : 
        print(i)