# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         if not head or not head.next:
#             return
#         #finding mid
#         fast = head
#         slow = head
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#         #taking ground mid in case of even condition
#         mid = slow
#         #reversing all the list after midr
#         p = None
#         q = mid
#         while q is not None:
#             r = q.next
#             q.next = p
#             p  = q
#             q = r
#         next_half_head = p
#         temp1 = head
#         temp2 = next_half_head
#         while next_half_head.next is not None:
#             temp1_next,temp2_next = temp1.next,temp2.next
#             temp1.next = temp2
#             temp2.next = temp1_next
#             temp1 = temp1_next
#             temp2 = temp2_next
#         if temp1:
#             temp1.next = None


# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# print("Original list:")
# printLinkedList(head)
# obj = Solution()
# obj.reorderList(head)
# print('reorderlist')
# printLinkedList(head)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        # Finding mid
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Taking ground mid in case of even condition
        mid = slow

        # Reversing all the list after mid
        p = None
        q = mid
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        next_half_head = p

        # Reordering the list
        temp1 = head
        temp2 = next_half_head
        while temp2:
            temp1_next, temp2_next = temp1.next, temp2.next

            temp1.next = temp2
            temp2.next = temp1_next

            temp1 = temp1_next
            temp2 = temp2_next

        # Set the next of the last node of the first half to None
        if temp1:
            temp1.next = None

# Helper function to print the linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create a linked list 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Print the original list
print("Original list:")
printLinkedList(head)

# Reorder the list
obj = Solution()
obj.reorderList(head)

# Print the reordered list
print('Reordered list:')
printLinkedList(head)
