from collections import Counter
class Solution:
   
    def sortByFreq(self,arr):
        c=Counter(arr)
        res=[]
        for k,v in sorted(c.items(),key=lambda x:(-x[1],x[0])):
            res.extend([k]*v)
        return res
