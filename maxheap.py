class queue:
    def __init__(self):
        self.q=[]
    def is_empty(self):
        return len(self.q)==0
    def length(self):
        return len(self.q)
    def right(self,index):
        return indedx*2 + 2
    def left(self,index):
        return indedx*2 + 1
    def parent(self,i):
        parent=(i-1)//2
        return parent
    def upheap(self,index):
        if index>0 and self.q[self.parent(index)]<self.q[index]:
            self.q[self.parent(index)],self.q[index]=self.q[index],self.q[self.parent(index)]
            self.upheap(self.parent(index))
    def add(self,val):
        self.q.append(val)
        self.upheap(self.length()-1)
    def dis(self):      
        print(self.q)
q=queue()
while True:
    print("Enter 1 For Add Item")
    '''print("Enter 2 For View Minimum")
    print("Enter 3 For Remove Item")
    print("Enter 4 For View Queue")'''
    print("Enter 5 For Exist")
    choice=int(input("Enter the Choice:"))
    if choice==1:
        p=int(input("Enter The prioity key:"))
        #v=input("Enter the Value:")
        q.add(p)
    elif choice==5:
        break
    elif choice==4:
        q.dis()
        
