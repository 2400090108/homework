class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        ans = []
        def dfs(x):
            if x == n:
                result.append(ans[:])
                return
            dfs(x + 1)
            ans.append(nums[x])
            dfs(x + 1)
            ans.pop()
        dfs(0)
        return result
