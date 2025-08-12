from collections import deque
q=deque()
def ins(node):
    if node is None:
        return
    o = que()
    o.enqueue(node)

    while q:
        current = o.dequeue()
        if current is None:
            continue
        print(f"Visited: {current.root}")
        if current.left:
            o.enqueue(current.left)
        if current.right:
            o.enqueue(current.right)
def display():
    print("Current Queue:", [node.root for node in q if node is not None])
class que:
    def enqueue(self,a):
        q.append(a)
    def dequeue(self):
        if not q:
            print("Queue is Empty")
            return
        q.popleft()
class tree:
    def __init__(self,node):
        self.root=node
        self.left=None
        self.right=None
root=tree("S")
N_A=tree("A")
N_B=tree("B")
N_C=tree("C")
N_D=tree("D")
N_E=tree("E")
N_F=tree("F")
root.left=N_A
root.rigth=N_B
N_A.left=N_C
N_A.rigth=N_D
N_B.left=N_E
N_B.rigth=N_F
ins(root)
display()


