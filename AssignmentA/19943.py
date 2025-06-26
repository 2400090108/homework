n, m = map(int, input().split())
ans = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    knot1, knot2 = map(int, input().split())
    ans[knot1][knot1] += 1
    ans[knot2][knot2] += 1
    ans[knot1][knot2] -= 1
    ans[knot2][knot1] -= 1
for j in range(n):
    print(' '.join(map(str, ans[j])))
