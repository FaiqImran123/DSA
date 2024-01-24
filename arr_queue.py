#2st approach to make queue ans shift as one value is remove no need to have front data member
class ArrQueue:
    def __init__(self, size):
        self.size =size
        self.arr =[None]*self.size
        self.rear =0
    def is_full(self):
        return self.rear ==self.size
    def is_empty(self):
        return self.rear==0
    def shift(self):
      

        for i in range((self.rear)-1):


            self.arr[i] =self.arr[i+1]
        self.rear-=1
    
    def push(self, val):
        
        if self.is_full()!=True:
            self.arr[self.rear]=val
            self.rear +=1
         
            

        else:
            raise Exception("List Full")
        

    def remove(self):
        
        if self.is_empty()!=True:
            self.shift()
  
        





        else:
            raise Exception("Empty List")


    def display(self):
        for i in range(self.rear):
            print(self.arr[i], end=" ")

        print()
def main():
    a =ArrQueue(4)
    a.push(90)
    a.push(80)
    a.push(89)
    a.push(67)
    a.display()
    a.remove()
    a.display()
    a.push(10000)
    a.display()
    a.remove()
    a.display()
    a.push(98)
    a.display()
    a.remove()
    a.display()
    a.push(9888)
    a.display()
 




main()