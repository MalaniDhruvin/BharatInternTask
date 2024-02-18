class node:
    def __init__(self,data):
        self.node=data
        self.left=None
        self.right=None

def inorder(root):
        if root:
            inorder(root.left)
            print(root.node,end=" ")
            inorder(root.right)
    
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print("\n{0}".format(root.node), end = " ")

def preorder(root):
     if root:
          print(root.node,end=" ")
          preorder(root.left)
          preorder(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

inorder(root)
postorder(root)
preorder(root)