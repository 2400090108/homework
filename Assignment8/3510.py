import heapq
from typing import List

class Node:
    def __init__(self, val: int, index: int):
        self.val = val
        self.prev = None
        self.next = None
        self.alive = True
        self.index = index

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # 初始化节点和双向链表
        nodes = [Node(nums[i], i) for i in range(n)]
        for i in range(n):
            if i > 0:
                nodes[i].prev = nodes[i - 1]
            else:
                nodes[i].prev = None
            if i < n - 1:
                nodes[i].next = nodes[i + 1]
            else:
                nodes[i].next = None

        # 计算初始逆序对数
        bad = 0
        for i in range(n - 1):
            if nodes[i].val > nodes[i + 1].val:
                bad += 1

        # 初始化堆
        heap = []
        for i in range(n - 1):
            current_node = nodes[i]
            next_node = current_node.next
            heapq.heappush(heap, (current_node.val + next_node.val, i))

        cnt = 0

        while bad > 0:
            if not heap:
                break  # 堆为空但仍有逆序对，说明逻辑错误

            s, i = heapq.heappop(heap)
            current_node = nodes[i]
            next_node = current_node.next

            # 检查 next_node 是否存在
            if next_node is None:
                continue

            # 跳过无效条目
            if not current_node.alive or not next_node.alive or (current_node.val + next_node.val) != s:
                continue

            prev_node = current_node.prev
            next_next_node = next_node.next

            # 移除旧逆序对
            # 1. prev_node 和 current_node 的逆序
            if prev_node and prev_node.alive and prev_node.val > current_node.val:
                bad -= 1
            # 2. current_node 和 next_node 的逆序
            if current_node.val > next_node.val:
                bad -= 1
            # 3. next_node 和 next_next_node 的逆序
            if next_next_node and next_next_node.alive and next_node.val > next_next_node.val:
                bad -= 1

            # 合并 next_node 到 current_node
            current_node.val += next_node.val
            next_node.alive = False

            # 更新指针
            current_node.next = next_next_node
            if next_next_node:
                next_next_node.prev = current_node
            else:
                current_node.next = None  # 确保指针正确

            # 添加新逆序对
            # 1. prev_node 和 current_node 的新逆序
            if prev_node and prev_node.alive and prev_node.val > current_node.val:
                bad += 1
            # 2. current_node 和 next_next_node 的新逆序
            if next_next_node and next_next_node.alive and current_node.val > next_next_node.val:
                bad += 1

            # 将新邻对推入堆
            if prev_node and prev_node.alive:
                heapq.heappush(heap, (prev_node.val + current_node.val, prev_node.index))
            if next_next_node and next_next_node.alive:
                heapq.heappush(heap, (current_node.val + next_next_node.val, current_node.index))

            cnt += 1

        return cnt

if __name__ == "__main__":
    s = Solution()
    print(s.minimumPairRemoval([5, 2, 3, 1]))  # 输出 2
    print(s.minimumPairRemoval([1, 2, 2]))     # 输出 0
    print(s.minimumPairRemoval([1, 1, 4, 4, 2, -4, -1]))  # 输出 5
    print(s.minimumPairRemoval([3,6,4,-6,2,-4,5,-7,-3,6,3,-4]))  # 输出 10
    print(s.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))  # 输出 9
    print(s.minimumPairRemoval([-1,2,2,-2,-3,0,2,1,0,0,1]))  # 输出 9
