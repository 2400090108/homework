def quadratic_probe_insert(keys, M):
    table = [None] * M
    result = []

    for key in keys:
        pos = key % M
        if table[pos] is None or table[pos] == key:
            table[pos] = key
            result.append(pos)
            continue

        i = 1
        inserted = False
        while not inserted:
            for sign in [1, -1]:
                new_pos = (pos + sign * (i ** 1)) % M
                if table[new_pos] is None or table[new_pos] == key:
                    table[new_pos] = key
                    result.append(new_pos)
                    inserted = True
                    break

            i += 1

    return result

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
keys = list(map(int, data[2 : 2 + N]))

positions = quadratic_probe_insert(keyss, M)
print(*positions)
