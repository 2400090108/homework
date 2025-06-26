class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n, m = len(matrix), len(matrix[0])
        road = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if matrix[i][j].isalpha():
                    road[matrix[i][j]].append((i, j))

        heap = [(0, 0, 0)]

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        dist = {}
        dist[(0, 0)] = 0
        tgt = (n - 1, m - 1)

        while heap:
            t, x, y = heappop(heap)
            if dist[(x, y)] < t:
                continue

            if (x, y) == tgt:
                return t

            w = matrix[x][y]
            if w.isalpha():
                while road[w]:
                    nx, ny = road[w].pop()
                    dist[(nx, ny)] = t
                    heappush(heap, (t, nx, ny))

            nt = t + 1
            for h in range(4):
                nx = x + dx[h]
                ny = y + dy[h]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if matrix[nx][ny] != '#' and ((nx, ny) not in dist or dist[(nx, ny)] > nt):
                    dist[(nx, ny)] = nt
                    heappush(heap, (nt, nx, ny))

        return -1

