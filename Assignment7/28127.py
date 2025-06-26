import sys
from collections import defaultdict


def process_icpc_results(m, submissions):
    teams = defaultdict(lambda: {'solved': set(), 'attempts': defaultdict(int), 'total_attempts': 0})

    for record in submissions:
        team_name, problem, result = record.split(',')
        team_name = team_name.strip()
        problem = problem.strip()
        result = result.strip()

        teams[team_name]['attempts'][problem] += 1
        teams[team_name]['total_attempts'] += 1

        if result == 'yes':
            teams[team_name]['solved'].add(problem)

    ranking = sorted(
        teams.items(),
        key=lambda item: (-len(item[1]['solved']), item[1]['total_attempts'], item[0])
    )

    for rank, (team_name, data) in enumerate(ranking[:12], start=1):
        print(rank, team_name, len(data['solved']), data['total_attempts'])


if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())
    submissions = [sys.stdin.readline().strip() for _ in range(m)]
    process_icpc_results(m, submissions)
