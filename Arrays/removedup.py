
def remove_duplicates(arr : list) : 
    has_seen = set() 
    output = list()

    for el in arr : 
        if el not in has_seen : 
            output.append(el)
            has_seen.add(el)

    return output

class IteratorClass (object) : 

    def __init__(self) : 
        self.num = 0

    def __iter__(self) : 
        self.index = 0 
        return self

    def __next__(self) : 
        if self.index <= 10 : 
            self.index+=1
            self.num += 10 
            return self.num
        else : 
            raise StopIteration
    


if __name__ == "__main__":
    arr = [1,2,3,4,5,1,2,4]
    arr = remove_duplicates(arr)
    print(arr)

    ob = IteratorClass()
    for i in ob : 
        print(i)

    