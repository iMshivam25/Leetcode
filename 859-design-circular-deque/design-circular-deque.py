class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.front = 0
        self.rear = 0
        self.occupied = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.size) % self.size  
        self.queue[self.front] = value                         
        self.occupied += 1                                        
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value                          
        self.rear = (self.rear + 1) % self.size                
        self.occupied += 1                                        
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None                          
        self.front = (self.front + 1) % self.size              
        self.occupied -= 1                                        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size    
        self.queue[self.rear] = None                           
        self.occupied -= 1                                        
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.occupied == 0

    def isFull(self) -> bool:
        return self.occupied == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()