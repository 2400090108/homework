from collections import deque
n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))
flag = k
res = []
while len(queue) >= 2:
    a = queue.popleft()
    queue.append(a)
    if k - 2 != 0:
        for _ in range(k-2):
            a = queue.popleft()
            queue.append(a)
    b = queue.popleft()
    res.append(b)
res_new = [str(i) for i in res]
print(" ".join(res_new))