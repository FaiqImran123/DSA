class Node:
    def __init__(self,val):
        self.data =val
        self.next =None
        self.prev =None

class AOL:
    def __init__(self):
        self.head =None
        self.tail =None
        self.size =0

    def add(self, val):
        n =Node(val)
        if self.head==None:
            self.head =n
            self.tail =n
        elif val<self.head.data:
            n.next =self.head
            self.head.prev =n
            self.head =n

        elif val>self.tail.data:
            self.tail.next =n
            n.prev =self.tail
            self.tail =n
        else:
            c =self.head
            while c!=None:
                if val<c.data:
                    temp =c.prev
                    c.prev.next =n
                    c.prev =n
                    n.next =c
                    n.prev =temp
                    return
                c =c.next
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
    def disp(self):
        c =self.head
        while c!=None:
            print(c.data, end=" ")
            c =c.next
        print()


def main():
    l =AOL()
    l.add(1)
    l.disp()
    l.add(0)
    l.disp()
    l.add(2)
    l.disp()
    l.add(1.5)
    l.disp()
    l.add(1.2)
    l.disp()
    l.add(1.8)
    l.disp()
    l.pop()
    l.disp()
    l.add_after(2,1.8)
    l.disp()
    l.add_before(3,1.2)
    l.disp()





main()
                    
