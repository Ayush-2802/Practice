from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
                self.size = [1] * size  # Track size of each connected component
        
            def Find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.Find(self.parent[i])  # Fixed variable 'x' to 'i'
                return self.parent[i]
    
            def Union(self, i, j):
                repi = self.Find(i)
                repj = self.Find(j)

                if repi != repj:
                    if self.rank[repi] < self.rank[repj]:
                        self.parent[repi] = repj
                        self.size[repj] += self.size[repi]  # Update size
                    elif self.rank[repi] > self.rank[repj]:
                        self.parent[repj] = repi
                        self.size[repi] += self.size[repj]  # Update size
                    else:
                        self.parent[repj] = repi
                        self.rank[repi] += 1
                        self.size[repi] += self.size[repj]  # Update size

        nums = set(nums)
        n = len(nums)
        nu = {num: i for i, num in enumerate(nums)}

        uf = UnionFind(n)
        for num in nums:
            if num + 1 in nums:
                uf.Union(nu[num], nu[num + 1])

        # Find the maximum size of connected components
        return max(uf.size) if nums else 0