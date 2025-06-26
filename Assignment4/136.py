class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):
            ans ^= nums[i]

        return ans
