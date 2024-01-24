#creating list using array
class List:
    def __init__(self, size):
        self.li =[-1]*size
        self.ind =0
    def append(self, val):
        self.li[self.ind] =val
        self.ind +=1

    def remove(self):
        val =self.li[self.ind-1]
        self.li[self.ind-1] =-1
        return val
    def is_empty(self):
        return self.ind==0
    def display(self):
        for i in range(self.ind):
            print(self.li[i], end=" ")
        print()
        

def main():
    li =List(100)
    print(li.is_empty())
    li.append(10)
    li.append(20)
    li.append(30)
    li.display()
    print(li.is_empty())


main()


