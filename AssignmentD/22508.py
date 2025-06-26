import sys
from collections import defaultdict, deque

def min_bonus(n, m, matches):
    graph = defaultdict(list)
    indegree = [0] * n

    for a, b in matches:
        graph[b].append(a)
        indegree[a] += 1

    bonus = [100] * n

    queue = deque([i for i in range(n) if indegree[i] == 0])

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if bonus[neighbor] <= bonus[curr]:
                bonus[neighbor] = bonus[curr] + 1
            indegree[neighbor] -=  1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sum(bonus)


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    matches = []
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        matches.append((a, b))
        idx += 2

    result = min_bonus(n, m, matches)
    print(result)
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]