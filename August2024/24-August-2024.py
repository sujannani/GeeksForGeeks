class Solution:
    def knapSack(self,W, wt, val):
        def rec(i,w):
            if i==0:
               if w+wt[i]<=W: return val[i]
               return 0
            pick = 0
            notPick = rec(i-1,w)
            if w+wt[i]<=W:
                pick = rec(i-1,w+wt[i]) + val[i]
            return max(pick,notPick)
        return rec(len(wt)-1,0) 