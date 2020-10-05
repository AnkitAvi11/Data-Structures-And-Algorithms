#   Stack using arrays

class Stack(object) : 

    def __init__(self) : 
        self.arr = list()

    def push(self, sk) : 
        self.arr.append(sk)

    def pop(self, index = None) : 
        if index is not None : 
            try : 
                return self.arr.pop(index)
            except : 
                pass
        else : 
            try : 
                return self.arr.pop()
            except IndexError as e : 
                return e

    def peek(self) : 
        return self.arr[len(self.arr) - 1]

    def isEmpty(self) : 
        return self.arr is None 

    def __repr__(self):
        return self.arr

    def __iter__(self) : 
        self.index = 0
        return self

    def __next__(self) : 
        if self.index < len(self.arr) : 
            return self.arr[self.index]
        self.index += 1

if __name__ == '__main__' : 
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    # for el in stack : 
    #     print(el)
    