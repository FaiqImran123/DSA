class Node:
    def __init__(self, val):
        self.data =val
        self.next =None
        self.prev =None


class CircularLinkedList:
    def __init__(self):
        self.head =None


    def add(self,o):
        n =Node(o)
        if self.head==None:
            self.head =n
            n.next =self.head
            n.prev =self.head
        else:
            c =self.head
            while True:
                if c.next==self.head:
                    break


                c =c.next

            c.next =n
            n.prev =c
            n.next =self.head
            self.head.prev =n
    def pop(self):
        if self.head ==None:
            raise Exception("Can't Pop value from empty list")
        elif self.head.next ==self.head:
            self.head =None
        else:
            c =self.head
            while True:
                if c.next==self.head:
                    break



                c =c.next
            tmp =c.prev
            c.prev.next =self.head
            self.head.prev =tmp
    def remove(self, val):   #remove given value
        if self.head==None:
            raise Exception("List is empty")
        elif self.head.data==val:
            


            if self.head.next==self.head:
                self.head =None
            else:
                temp =self.head
                self.head =self.head.next
                self.head.prev =temp.prev
                temp.prev.next =self.head
       
            
            
        else:
            c =self.head
            while True:
                if c.data==val:
                    c.prev.next =c.next
                    c.next.prev =c.prev
                    return
                c =c.next

            raise Exception("Not found")
    def display(self):
        if self.head==None:
            raise Exception("List is empty")
        else:
            c =self.head
            while True:
                print(c.data, end=" ")

                c =c.next

                if c==self.head:
                    break
            print()
        
    def add_after(self, v1,v2):    #inset v1 after v2
        n =Node(v1)
        if self.head==None:
            raise Exception("Empty List")

        else:
            c =self.head
            while True:
                if c.data==v2:
                 
                    temp =c.next
                    c.next =n
                    n.prev =c
                    n.next =temp
                    return
                if c.next==self.head:
                    break
                c =c.next
            raise Exception("Not Found")

    def add_before(self,v1, v2):  #insert v1 before v2
        n =Node(v1)
        if self.head==None:
            raise Exception("Not found")  
        else:
            c =self.head
            while True:
                if c.data==v2:
               
                    if c ==self.head:
                        temp =c.prev
                        c.prev.next =n
                        n.next =c
                        n.prev =temp
                        c.prev =n
                        self.head =n
                        return
                    else:
                        temp =c.prev
                        c.prev.next =n
                        n.next =c
                        n.prev =temp
                        c.prev =n
                        return
                if c.next==self.head:
                    break
                c =c.next
            raise Exception("Not Found")           
                    


def main():
    c =CircularLinkedList()
    c.add(10)
    c.add(20)
    c.add(30)
    c.display()
    c.remove(20)
   
    c.display()
    c.add_before(10,10)
    c.display()
    c.add_after(100,10)
    c.add_after(99,30)
    c.add_after(78,10)
    c.display()
 
    

main()
