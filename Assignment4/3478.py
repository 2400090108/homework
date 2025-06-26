class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        combined = defaultdict(list)
        for num1, num2 in zip(nums1, nums2):
            combined[num1].append(num2)
        heap, cur, res = [], 0, {}
        for num1 in sorted(combined.keys()):
            res[num1] = cur
            for num2 in combined[num1]:
                heapq.heappush(heap, num2)
                cur += num2
                if len(heap) > k :
                    cur -= heapq.heappop(heap)
        return list(map(lambda x: res[x], nums1))
