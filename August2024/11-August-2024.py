class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x.deadline)
        n = len(Jobs)
        result = []
        maxHeap = []
        for i in range(n - 1, -1, -1):
            if i == 0:
                slots_available = Jobs[i].deadline
            else:
                slots_available = Jobs[i].deadline - Jobs[i - 1].deadline
            heapq.heappush(maxHeap, (-Jobs[i].profit, Jobs[i].deadline, Jobs[i].id))
            while slots_available and maxHeap:
                profit, deadline, job_id = heapq.heappop(maxHeap)
                slots_available -= 1
                result.append([job_id, deadline,profit])
        profit=0
        for i in result:
            profit+=-i[2]
        return [len(result),profit]