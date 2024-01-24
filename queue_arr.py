class Queue:
    def __init__(self, size):
        self.queue =[-1]*size
        self.start_ind =0
        self.end_ind =0


    def enqueue(self, val):
        self.queue[self.end_ind] =val
        self.end_ind +=1

    def dequeue(self):
        val =self.queue[self.start_ind]
        self.start_ind +=1
        return val
    def is_empty(self):
        return self.start_ind==self.end_ind
    def display(self):
        if self.start_ind==self.end_ind:
            raise Exception("Empty List")
        for i in range(self.start_ind, self.end_ind):
            print(self.queue[i], end=" ")
        print()
def main():
    q =Queue(100)
    q.enqueue(10)
    q.enqueue(40)
    q.enqueue(50)
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    print(q.is_empty())
    q.display()



main()

