class Solution(object):
    def isPalindrome(self, x):
        rev=0
        i=-1
        y=x
        while y>0:
            y//=10
            i+=1
        print(i)
        y=x
        while(x>0):
            rev+=(10**i)*(x%10)
            i-=1
            x//=10
        if y==rev:
            return "true"
        else:
            return "false"
s=Solution()
print(s.isPalindrome(121))
