class ListNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyQueue(object):
    def __init__(self):
        ''' First-in-first-out (LIFO)
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
            cur.prev = self.tail
            self.tail.next = cur
            self.tail = cur
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
        

    def peek(self):
        """
        :rtype: int
        """
        return self.head.val
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.count==0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()