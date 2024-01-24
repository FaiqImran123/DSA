#stack using list
class Stack:
    def __init__(self, size):
        self.stack =[-1]*size
        self.ind =0

    def push(self, val):
        self.stack[self.ind] =val
        self.ind +=1
    def pop(self):
        self.ind -=1
        val =self.stack[self.ind]
        self.stack[self.ind] =-1
        return val
    def get_top(self):
        return self.stack[self.ind-1]
    def display(self):
        for i in range(self.ind-1, -1, -1):
            print(self.stack[i], end=" ")
        print()       

def main():
    s =Stack(100)
    s.push(10)
    s.push(30)
    s.push(12)
    print(s.get_top())
    s.display()




main() 
