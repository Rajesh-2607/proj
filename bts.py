class Bst:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
    def add(self,newnode):
        if self is None:
            return
        if(newnode.data > self.data):
            if self.right is None:
                self.right=newnode
            else:
                self.right.add(newnode)
        else:
            if self.left is None:
                self.left=newnode
            else:
                self.left.add(newnode)
        return
def inorder(self):
        if self is None:
            return
        inorder(self.left)
        print(self.data,end=" ")
        inorder(self.right)
x=int(input("No of Elements to be inserted:"))
ele=[]
for i in range(x):
    ele.append(int(input()))
root=Bst(ele[0])
for i in range(1,x):
    root.add(Bst(ele[i]))
inorder(root)
