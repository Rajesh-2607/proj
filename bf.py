tree={
    'A':['B','C'],
    'B':['E','D'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    }
#to store visited nodes
visitednodes=[]
#to store nodes in queue
queuenodes=[]
#function
def bfs(visitednodes,tree,snode):
    visitednodes.append(snode)
    queuenodes.append(snode)
    print()
    print("RESULT")
    while queuenodes:
        s=queuenodes.pop(0)
        print(s,end=" ")
        for neighbour in tree[s]:
            if neighbour not in visitednodes:
                visitednodes.append(neighbour)
                queuenodes.append(neighbour)
snode=input("enter starting node(A,B,C,D or E):").upper()
bfs (visitednodes,tree,snode)
