class Node:
    def __init__(self,val):
        self.data =val
        self.next =None

class LinkedList:

    def __init__(self):
        self.head =None
        self.tail =None
        self.size =0


    def push(self,val):
        n = Node(val)
        if self.head==None:
            self.head =n
            self.tail =n
        else:
            self.tail.next =n
            self.tail =n
        self.size +=1

    def pop(self):
        self.size-=1
        if self.head==None:

            raise Exception("Can't Pop from empty List")
        elif self.head.next==None:
            temp =self.head.data
            self.head =None
            self.tail =None
        else:
            c =self.head
            while c.next.next!=None:
                c =c.next
            tmp =c.next.data
            c.next =None
            self.tail =c
            return tmp
    def add_after(self,val1, val2):   #insert val1 after val2
        self.size +=1
        if self.head==None:
            raise Exception("List is empty")
        else:
            n =Node(val1)
            c =self.head
            while c!=None:
                if c.data==val2:
                    t =c.next
                    c.next =n
                    n.next =t
                    return
                c =c.next
            raise Exception("Not found")
    def add_before(self,val1,val2):   #insert val1 before val2
        self.size+=1
        n =Node(val1)
        if self.head==None:
            raise Exception("List is empty")
        elif self.head.data==val2:
            n.next =self.head
            self.head =n
        else:
        
            c =self.head
            while c.next!=None:
                if c.next.data==val2:
                    t =c.next
                    c.next =n
                    n.next =t
                    return
                c =c.next

            raise Exception("Not found a val")


               

         
  


    def disp(self):
        c =self.head
        while c!=None:
            print(c.data, end=" ")
            c =c.next
        print()

def main():


    l =LinkedList()
    l.push(10)
    l.add_before(2,10)
    l.add_before(11,10)
    l.push(5)
    l.push(20)


    l.disp()
    l.pop()
    l.disp()
   
    l.add_after(100,5)
    l.add_after(2,10)
    l.add_before(90,10)
    l.add_before(10,90)

    print("-----")
    l.disp()
    print("-")
    l.add_before(100000,90)
    l.add_before(0,100)
    
    
    l.disp()

 
 
    #l.add_after(80,19)
    #l.add_after(10000000,73)
    print("---")
    #l.disp()





main()

