tar = int(input())
s = [int(x) for x in input().split()]
s.sort()

ans = 200000
gap = 100000 - 2

h = 0
t = len(s) - 1
while h < t:
    mid = s[h] + s[t]
    if mid == tar:
        ans = mid
        break

    if abs(mid - tar) < gap:
        gap = abs(mid - tar)
        ans = mid

    if abs(mid - tar) == gap:
        ans = min(ans, mid)

    if mid > tar:
        t -= 1
    elif mid < tar:
        h += 1

print(ans)