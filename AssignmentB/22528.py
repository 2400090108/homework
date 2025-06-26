def is_ok(b, scores):
    a = b / 1e9
    cnt = 0
    threshold = 0.6 * len(scores)
    for x in scores:
        new_score = a * x + 1.1 ** (a * x)
        if new_score >= 85:
            cnt += 1
    return cnt >= threshold


def main():
    scores = [float(x) for x in input().split()]

    l, r = 1, 10 ** 9 + 1
    ans = -1
    while l < r:
        mid = (l + r) // 2
        if is_ok(mid, scores):
            ans = mid
            r = mid
        else:
            l = mid + 1

    print(ans)


if __name__ == "__main__":
    main()
