from queue import Empty
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def addqueue(self,data):
        if self.rear is None:
            self.front = self.rear= Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
    def removequeu(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            value = self.front.data
            self.front = self.front.next
            return value
    def __len__(self):
        return self.size()
    def isempty(self):
        return self.size == 0

    def size(self):
        count = 0
        current = self.front
        while(current):
            count+=1
            current = current.next
        return print("size is : ", count)
    def Front(self):
        if self.front is None:
            print("queue is empty")
        else:
            sd = self.front
            return print("Front is : ", sd.data)
    def Rear(self):
        if self.rear is None:
            print("queue is empty")
        else:
            ssd = self.rear
            return print("Rear is : ", ssd.data)
    def display(self):
        ds = self.front
        while ds:
            print(ds.data, end=" ====> ")
            ds = ds.next
        print()






q = queue()
q.addqueue(20)
q.addqueue(40)
q.addqueue(50)
q.addqueue(80)
# q.removequeu()
q.Rear()
q.Front()
q.display()