class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def __init__(self):
        self.head = None


    def insert_at_tail(self,key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode 


    def printList(self):
        if self.head is None:
            print('The list is empty')
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next 
          
    def addTwoNumbers(self,l1,l2):
        carry = 0
        sum_list = Solution()
        temp1 = l1.head
        temp2 = l2.head
        while temp1 is not None or temp2 is not None or carry != 0:
            first_val = 0
            if temp1 != None:
                first_val = temp1.data
            second_val = 0
            if temp2 != None:
                second_val = temp2.data
            
            key = first_val + second_val + carry 
            carry = key // 10
            val = key % 10
            sum_list = self.insert_at_tail(val)
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        

        return sum_list
    
obj = Solution()
obj.insert_at_tail(2)
obj.insert_at_tail(4)
obj.insert_at_tail(3)

obj2 = Solution()
obj2.insert_at_tail(5)
obj2.insert_at_tail(6)
obj2.insert_at_tail(4)
obj2.insert_at_tail(4)
obj2.insert_at_tail(4)
obj2.insert_at_tail(4)

obj3 = Solution()
obj3.addTwoNumbers(obj,obj2)
obj3.printList()


