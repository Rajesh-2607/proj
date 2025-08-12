class Solution(object):
    def __init__(self):
        self.s1=0
        self.s2=0
        self.l=[]
    def addTwoNumbers(self, l1, l2):
        for i in range(len(l1)-1,-1,-1):
            self.s1+=(10**i)*l1[i]
        for i in range(len(l2)-1,-1,-1):
            self.s2+=(10**i)*l2[i]
        sum_=self.s2+self.s1
        print(sum_)
        if sum_==0:
            return [0]
        else:
            while(sum_>0):
                self.l.append(sum_%10)
                sum_//=10
        return self.l
l1=[1,2,3]
l2=[2,8,3]
obj=Solution()
print(obj.addTwoNumbers(l1,l2))
