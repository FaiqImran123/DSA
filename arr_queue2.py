#3st approach to make queue shift no space left and required both front and back
class ArrQueue:
    def __init__(self, size):
        self.size =size
        self.arr =[None]*self.size
        self.front=0
        self.rear =0
    def is_full(self):
        return self.rear-self.front ==self.size
    def is_empty(self):
        return self.rear==self.front
    def shift(self):
        

        for i in range(0, (self.rear-self.front)):

            self.arr[i] =self.arr[self.front+i]
            
        val =self.front
        self.front =0
        self.rear -=val
     
    
    def push(self, val):
    
        if self.is_full()!=True:
    
            self.arr[self.rear]=val
            self.rear +=1
            if self.rear==self.size and self.front!=0:
                self.shift()


        else:
            raise Exception("List Full")
        

    def remove(self):
        if self.is_empty()!=True:
            self.front +=1
            if self.rear==self.size and self.front!=0:
                self.shift()

  
        





        else:
            raise Exception("Empty List")


    def display(self):
        for i in range(self.front, self.rear):
            print(self.arr[i], end=" ")

        print()
def main():
    a =ArrQueue(4)
    a.push(90)
    a.remove()


    a.push(89)
    a.push(67)
    a.push(98)
    a.push(100)
    a.display()
    a.remove()
    a.remove()
    a.display()
    a.push(10000)
    a.display()
    a.remove()
    a.display()
    a.push(98)
    a.display()
 




main()