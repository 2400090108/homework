n, k = map(int, input().split())
cows = []
for i in range(n):
    a, b = map(int, input().split())
    cows.append((a, b, i + 1))
cows.sort(key = lambda x : x[0], reverse = True)
second_round_cows = cows[:k]
second_round_cows.sort(key = lambda x : x[1], reverse = True)
print(second_round_cows[0][2])