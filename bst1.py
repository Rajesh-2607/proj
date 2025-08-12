class Bst:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, newnode):
        if newnode.data > self.data:
            if self.right is None:
                self.right = newnode
            else:
                self.right.add(newnode)
        else:
            if self.left is None:
                self.left = newnode
            else:
                self.left.add(newnode)

n = int(input("No of Elements to be inserted: "))
ele = []

for i in range(n):
    ele.append(int(input(f"Enter element {i+1}: ")))
root = Bst(ele[0])
for i in range(1, n):
    root.add(Bst(ele[i]))

# Optional: Inorder traversal to display the BST
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

print("Inorder Traversal of BST:")
inorder(root)
