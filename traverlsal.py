class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_traversal(root):

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

def post_order_traversal(root):
    if root is None:
        return
    stack = []
    stack.append((root,False))
    while stack:
        
        node,visited = stack.pop()
        if visited:
            print(node.data)
        else:
            stack.append((node,True))
            if node.right:
                stack.append((node.right,False))
            if node.left:
                stack.append((node.left,False))
        
def inorder_traversal(root):
    if root is None :
        return
    stack = []
    stack.append((root,False)) 
    while stack :
        node,visited= stack.pop()
        if visited :
            print(node.data)
        else:
            if node.right:
                stack.append((node.right,False))
            
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        for i in range(len(stack)):
            print(stack[i][0].data)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(inorder_traversal(root))
            
