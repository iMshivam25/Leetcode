class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:        
        for x,y in self.overlaps:
            if start<y and end>x:
                return False
        for x,y in self.bookings:
            if start<y and end>x:
                self.overlaps.append([max(x,start),min(y,end)])
        self.bookings.append([start,end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)