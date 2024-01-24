class Priority_Queue:
    class Queue:
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


    def __init__(self, size=100):
        self.priority =4
        self.arr =[0]*self.priority
        for i in range(self.priority):
            self.arr[i] =self.Queue(size)

    def insert(self, val, priority):
        if self.arr[priority].is_full()!=True:
            self.arr[priority].push(val)
        else:
            raise Exception("No space")
    def remove(self):
        for i in range(self.priority-1, -1,-1):
            if self.arr[i].is_empty()!=True:
                self.arr[i].remove()
                break
    def display(self):
        for i in range(self.priority-1,-1,-1):
            self.arr[i].display()
    

    

def main():
    p =Priority_Queue(3)
    p.insert(20, 0)
    p.insert(30,1)
    

    
    p.insert(87, 2)
    p.insert(98,2)
    p.insert(78,2)
    p.insert(98, 3)
    p.remove()

  
    p.display()



main()

        



 