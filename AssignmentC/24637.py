import sys
sys.setrecursionlimit(10**7)

def max_treasure(N, vals):
    f0 = [0] * (N + 1)
    f1 = [0] * (N + 1)

    for i in range(N, 0, -1):
        l, r = 2 * i, 2 * i + 1

        include = vals[i]
        if l <= N:
            include += f0[l]
        if r <= N:
            include += f0[r]
        f1[i] = include

        not_include = 0
        if l <= N:
            not_include += max(f0[l], f1[l])
        if r <= N:
            not_include += max(f0[r], f1[r])
        f0[i] = not_include

    return max(f0[l], f1[l])

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    vals = [0] + list(map(int, data[1:]))
    print(max_treasure(N, vals))