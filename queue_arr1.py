class Queue:
    def __init__(self, size):
        self.queue =[-1]*size
        self.start_ind =size-1
        self.end_ind =size-1


    def push(self, val):
        self.queue[self.end_ind] =val
        self.end_ind -=1

    def pop(self):
        val =self.queue[self.start_ind]
        self.start_ind -=1

        return val
    def is_empty(self):
        return self.start_ind==self.end_ind
    def disp(self):
        if self.start_ind==self.end_ind:
            raise Exception("Empty List")
        for i in range(self.start_ind, self.end_ind, -1):
            print(self.queue[i], end=" ")
        print()
def main():
    q =Queue(100)
    q.push(10)
    q.push(40)
    q.push(50)
    q.disp()
    q.pop()
    q.pop()
   

    print(q.is_empty())
    q.disp()



main()

