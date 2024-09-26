class MyCalendar:
    def __init__(self):
        self.date = []

    def book(self, start: int, end: int) -> bool:
        temp = [start,end]
        for item in self.date:
            if start<item[-1] and end>item[0]:
                break
        else:
            self.date.append(temp)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)