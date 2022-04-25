class ListNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack(object):
    def __init__(self):
        ''' Last-in-first-out (LIFO)
        '''
        self.head = None
        self.tail = None
        self.count = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        cur = ListNode(x)
        if self.count==0:
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
        self.count+=1
        

    def pop(self):
        """
        :rtype: int
        """
        if self.count==0:
            return False
            
        elif self.count==1:
            cur = self.tail
            self.head = None
            self.tail = None
        else:
            cur = self.head
            self.head = self.head.next
            self.head.prev = None
        self.count-=1
        curVal = cur.val
        del cur
        return curVal

    def top(self):
        """
        :rtype: int
        """
        return self.head.val
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.count==0
        


# Your MyStack object will be instantiated and called as such:
if __name__=="__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(3)
    obj.push(4)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    print(param_2, param_3, param_4)