import sys


def matrix_transpose(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]


def matrix_multiply(A, B):
    a_rows, a_cols = len(A), len(A[0])
    b_cols = len(B[0])
    C = [[0] * b_cols for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                C[i][j] += A[i][k] * B[k][j]
    return C


def print_matrix(matrix):
    for row in matrix:
        print(''.join(f'{num:5}' for num in row))


def main():
    x1, y1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(x1)]

    x2, y2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(x2)]

    if y1 == x2:
        C = matrix_multiply(A, B)
        result = matrix_transpose(C)
    else:
        result = matrix_transpose(A)

    print_matrix(result)


if __name__ == "__main__":
    main()
