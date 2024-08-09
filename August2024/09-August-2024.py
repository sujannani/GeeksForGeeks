class Solution:
    def Maximize(self, arr): 
        # Complete the function
        arr.sort()
        res=0
        for i in range(len(arr)):
            res+=i*arr[i]
            res=res%1000000007
        return res%1000000007