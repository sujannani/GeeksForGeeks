from collections import deque,defaultdict
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        graph=defaultdict(list)
        for i in range(n):
            graph[i]=[]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        que=deque()
        res=[float('inf')]*n
        que.append(src)
        res[src]=0
        while que:
            x=que.popleft()
            for node in graph[x]:
                if 1+res[x]<res[node]:
                    res[node]=1+res[x]
                    que.append(node)
        for i in range(len(res)):
            if res[i]==float('inf'):
                res[i]=-1
        return res