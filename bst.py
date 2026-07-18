class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert(key ,data):
        if key.data is None :
            return 'key not found'
        if key.data == data:
            return 'found'
        
        if data > key.data :
            return insert(key.right,data)
        else :
            return insert(key.left,data)
        
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
def find_inorder_prec(root):
    while root.right is not None:
        root = root.right
    return root
def delete_node(root,key):
    if root is None :
        return 'not present'
    if root.data == key:
        if root.right is None and root.left is None :
            root = None
            return root
        elif root.left is None:
            root = root.right 
        elif root.right is None:
            root = root.left
        else :
            inorder_prec = find_inorder_prec(root.left)
            root.data = inorder_prec.data
            root.left = delete_node(root.left, inorder_prec.data)
    elif key > root.data:
        root.right = delete_node(root.right,key)
    else:
        root.left = delete_node(root.left,key)
    return root


def create_bst_from_preorder(preorder):

    stack = []
    
    root = Node(preorder[0])
    stack.append(root)
    for val in preorder[1:]:
        if val < stack[-1].data:
            stack[-1].left = Node(val)
            stack.append(stack[-1].left)
            
        else:
            while stack and  val > stack[-1].data:
                rightn = stack.pop()
            rightn.right = Node(val)
            stack.append(rightn.right)

    return root





    
            

def inorder(root):
    if root is None :
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
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

# create_bst_from_preorder([])
# # delete_node(root,33)
# (inorder(root))

preorder = [5, 2, 3, 6, 44, 33, 34, 73]

root = create_bst_from_preorder(preorder)

inorder(root)