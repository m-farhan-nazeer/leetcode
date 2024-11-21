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

    def swap_pairs(self):
        temp = self.head
        while temp is not None and temp.next is not None:
            # Swapping values of adjacent nodes
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

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
obj2.insert_at_tail(4)
obj2.insert_at_tail(44)
obj2.insert_at_tail(6)
#obj2.insert_at_tail(49)
obj2.printList()
obj2.swap_pairs()
obj2.printList()
