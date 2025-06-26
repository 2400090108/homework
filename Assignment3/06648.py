import heapq

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    seq1 = sorted(map(int, input().split()))
    for _ in range(m - 1):
        seq2 = sorted(map(int, input().split()))

        min_heap = [(seq1[i] + seq2[0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)
        result = []
        for _ in range(n):
            current_sum, i, j = heapq.heappop(min_heap)
            result.append(current_sum)
            if j + 1 < len(seq2):
                heapq.heappush(min_heap, (seq1[i] + seq2[j + 1], i, j + 1))
        seq1 = result
    print(*seq1)
