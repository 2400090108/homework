from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                uf.union(i, i + 1)

        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res
