def josephus(n, p, m):
    if n == 1:
        return [1]

    out_order = []
    pos = p - 1
    kids = list(range(1, n+1))

    while len(kids) > 0:
        pos = (pos + m - 1) % len(kids)
        out_order.append(kids.pop(pos))

    return out_order

while True:
    n, p, m = map(int, input().split())
    if n + p + m == 0:
        break
    result = josephus(n, p, m)
    print(','.join(map(str, result)))