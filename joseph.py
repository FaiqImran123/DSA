#header node handles boundary cases easily
class Node:
    def __init__(self, val):
        self.data =val
        self.next =None
class LinkedList:

    def __init__(self):
        self.head =None
        self.tail =None
        self.size =0


    def add(self,val):
        n = Node(val)
        if self.head==None:
            self.head =n
            self.tail =n
            self.head.next=self.tail


        else:
            self.tail.next =n
            self.tail =n
            n.next =self.head
        self.size +=1

    def remove(self, val):
        if self.head.next==None:
            raise Exception("Empty")
        elif self.head.data==val:
            self.head =self.head.next
            self.tail.next=self.head
            self.size -=1

        else:
            c =self.head
            while c.next!=None:
                if c.next.data==val:

                    c.next =c.next.next
                    if c.next.next==self.head:
                        self.tail =c
                    self.size -=1
                    return
            
                c =c.next
            raise Exception("Not found")
            

        
    def dis(self):
        c= self.head
        while True:
            print(c.data, end=" ")
            c =c.next
        
            if c==self.head:
                break


        print()
    def kill(self, K):
        x =1
        if self.head==None:
            raise Exception("No person in circle")
        else:
            c =self.head

            while self.size>1:
                x =1
            
                
                
                while x!=K:
                    x +=1
                    c =c.next
                    
               
                tmp =c.data
             
                c =c.next
             
                self.remove(tmp)
               
                print(f"{tmp} has been killed")
                
                
        
            print(self.head.data)
            return self.head.data


def main():
    l =LinkedList()
    l.add(10)
    l.add(12)
    l.add(13)
    l.add(14)
    l.dis()
    

    l.kill(10)




main()