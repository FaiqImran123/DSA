class Node:
    def __init__(self,val):
        self.data =val
        self.link =None
class LinkedStacks:
    def __init__(self):
        self.head =None
    
    def push(self,val):
        tmp =Node(val)
        if self.head==None:
            self.head =tmp
            
        else:
            tmp.link =self.head
            self.head =tmp
    def pop(self):
        if self.head==None:
            return 0
        else:
            tmp =self.head
            self.head =self.head.link
            return tmp.data
    def peak(self):
        if self.head==None:
            return
        return self.head.data

    def is_empty(self):
        return self.head==None


def main():
    user =input("Enter Your Exp: ")
    l =LinkedStacks()
    for i in range(len(user)):
        if user[i] in ["[","(","{"]:
            l.push(user[i])
        else:

            if l.is_empty==True:
                return False
            else:
                top =l.peak()
                if top=="[" and user[i]=="]":
                    
                    l.pop()
                        
                elif top=="(" and user[i]==")":

                    l.pop()
                elif top=="{" and user[i]=="}":
              
                    l.pop()
            
                else:
                    return False

    if l.is_empty()==True:
        return True
    else:
        return False





print(main())