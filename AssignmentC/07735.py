import heapq
from collections import defaultdict

MAX_COINS = int(input())
CITY_COUNT = int(input())
ROAD_COUNT = int(input())

roads = defaultdict(list)

for _ in range(ROAD_COUNT):
    start, end, lenght, money = map(int, input().split())
    start, end = start - 1, end - 1
    roads[start].append((end, lenght, money))

def bfs(start, end, max_coins):
    queue = [(0, max_coins, start)]
    visited = set()

    while queue:
        distance, coins, city = heapq.heappop(queue)

        if city == end:
            return distance

        visited.add((city, coins))

        for next_city, road_lenght, road_money in roads[city]:
            if coins >= road_money:
                new_distance = distance + road_lenght
                if (next_city, coins - road_money) not in visited:
                    heapq.heappush(queue, (new_distance, coins - road_money, next_city))

    return -1

print(bfs(0, CITY_COUNT - 1, MAX_COINS))