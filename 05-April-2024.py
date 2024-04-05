class Solution:
	def min_operations(self,nums):
        def longIncSubSeq(nums):
            dp = [1] * (len(nums))
            for i in range(1,len(nums)):
                for j in range(i):
                    if(nums[j]<nums[i]) and (nums[i]-nums[j])>=(i-j):
                        dp[i] = max(dp[i],1+dp[j])
            return max(dp)
        ans = len(nums)-longIncSubSeq(nums)
        return ans