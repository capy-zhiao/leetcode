class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = ListNode(val)
        cur = self.head
        if cur == None:
            self.head = newnode
        else:
            while cur.next:
                cur = cur.next
            cur.next = newnode
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if(index == self.size):
            self.addAtTail(val)
        elif(index > self.size):
            return
        elif (index == 0):
            self.addAtHead(val)
        else:
            cur = self.head
            newnode = ListNode(val)
            for _ in range(index-1):
                cur = cur.next
            newnode.next = cur.next
            cur.next = newnode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1

MyLinkedList().addAtHead(5)