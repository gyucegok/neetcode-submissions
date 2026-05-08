class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None        


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while i<index and curr:
            i += 1
            curr = curr.next
        if curr:
            return curr.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        curr = ListNode(val)
        curr.next = self.head.next
        self.head.next = curr

        if self.tail == self.head:
            self.tail = curr


    def insertTail(self, val: int) -> None:
        curr = ListNode(val)
        self.tail.next = curr
        self.tail = curr

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i<index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False


    def getValues(self) -> List[int]:
        a = []
        curr = self.head.next
        while curr:
            a.append(curr.val)
            curr = curr.next
        return a

