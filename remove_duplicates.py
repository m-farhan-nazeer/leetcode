class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
            
    

    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return  # No duplicates possible in an empty list or a list with one element

        dummy = Node(0)
        dummy.next = self.head
        pre = dummy
        temp = self.head

        while temp and temp.next:
            if temp.data == temp.next.data:
                val_to_remove = temp.data
                # Skip all nodes with the same value as val_to_remove
                while temp and temp.data == val_to_remove:
                    temp = temp.next
                # Remove all nodes with the value val_to_remove
                pre.next = temp
            else:
                pre = temp
                temp = temp.next

        self.head = dummy.next
        print()  # Add a new line after printing the list
    def printList(self):
        if self.head is None:
            print('The list is empty')
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=',')
            currentNode = currentNode.next
        print()  # Add a new line after printing the list
obj2 = Solution()
obj2.insert_at_tail(5)
obj2.insert_at_tail(6)
obj2.insert_at_tail(10)
obj2.insert_at_tail(10)
obj2.insert_at_tail(10)
obj2.insert_at_tail(11)
obj2.insert_at_tail(13)
obj2.insert_at_tail(13)
obj2.insert_at_tail(13)
obj2.insert_at_tail(13)
obj2.insert_at_tail(15)
#obj2.insert_at_tail(49)
obj2.printList()
obj2.remove_duplicates()
obj2.printList()
