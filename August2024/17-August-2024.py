class Solution:
    def productExceptSelf(self, nums):
        #code here
        suffix=[0]*(len(nums)+1)
        prefix=[0]*(len(nums)+1)
        suffix[0]=1
        prefix[-1]=1
        for i in range(1,len(nums)+1):
            suffix[i]=suffix[i-1]*nums[i-1]
        for j in range(len(nums)-1,-1,-1):
            prefix[j]=prefix[j+1]*nums[j]
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=suffix[i]*prefix[i+1]
        return res