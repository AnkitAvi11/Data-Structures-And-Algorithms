
#   program to demostrate how iterator in python works


class MyIterator : 

    def __iter__(self) : 
        self.num = 0
        return self


    def __next__(self) : 
        self.num += 1
        if self.num <= 10 : 
            return self.num
        
        else : 
            raise StopIteration

        



if __name__ == '__main__' : 
    ob = MyIterator()

    for i in ob :
        print(i)

    