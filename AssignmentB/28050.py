import sys


def is_valid_move(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def get_degree(x, y, board, n, moves):
    count = 0
    for dx, dy in moves:
        if is_valid_move(x + dx, y + dy, board, n):
            count += 1
    return count


def knights_tour_warnsdorff(n, sr, sc):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[sr][sc] = 0

    def backtrack(x, y, move_count):
        if move_count == n * n:
            return True

        next_moves = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, board, n):
                degree = get_degree(nx, ny, board, n, moves)
                next_moves.append((degree, nx, ny))

        next_moves.sort()

        for _, nx, ny in next_moves:
            board[nx][ny] = move_count
            if backtrack(nx, ny, move_count + 1):
                return True
            board[nx][ny] = -1

        return False

    if backtrack(sr, sc, 1):
        print("success")
    else:
        print("fail")


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    sr, sc = map(int, sys.stdin.readline().strip().split())
    knights_tour_warnsdorff(n, sr, sc)
