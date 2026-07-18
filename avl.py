
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def create_bst(root,data):
    if root is None:
        root = Node(data)
        return root
    if data == root.data:
        return root
    if data > root.data:
        root.right =  create_bst(root.right , data)
    else:

        root.left = create_bst(root.left , data)
    return root

def find_height(root):
    if root is None:
        return 0
    height = 1 + max(find_height(root.left),find_height(root.right))
    return height




root = None 
root = create_bst(root,5)
root = create_bst(root,6 )
root= create_bst(root ,2)
root = create_bst(root ,44)

root = create_bst(root ,6)

root = create_bst(root ,3)
root = create_bst(root ,33)
root = create_bst(root ,34)
root = create_bst(root ,73)

print(find_height(root))