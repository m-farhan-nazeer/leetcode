class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def length(self, head: ListNode) -> int:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    def reorderList(self, head: ListNode) -> None:
        if not head or head.next is None:
            return
        index = 1
        l = self.length(head)
        r = l//2
        for i in range(r):
            temp1 = head
            for _ in range(index):
                temp1 = temp1.next
            temp2 = head
            for _ in range(l):
                temp2 = temp2.next
            temp2.next = temp1.next
            temp1.next = temp2
            index = index + 2
            l = l - 1
        return(head)
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
    

        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Find the middle of the linked list
        mid_index = length // 2
        temp1 = head
        for _ in range(mid_index):
            temp1 = temp1.next

        # Step 3: Reverse the second half of the linked list
        prev = None
        temp2 = temp1.next
        while temp2:
            next_node = temp2.next
            temp2.next = prev
            prev = temp2
            temp2 = next_node

        # Step 4: Merge the first half and the reversed second half alternately
        temp1.next = prev
        current = head
        temp1 = temp1.next
        while temp1:
            next_node = current.next
            current.next = temp1
            current = temp1
            temp1 = next_node

    # Handle the case when the length of the original list is odd
        current.next = None


def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print("Original list:")
printLinkedList(head)
obj = Solution()
obj.reorderList(head)
print('reorderlist')
printLinkedList(head)