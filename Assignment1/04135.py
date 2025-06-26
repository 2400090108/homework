def minMaxMonthlyExpense(N, M, expenses):
    def can_split(max_expense):

        months = 1
        current_sum = 0
        for cost in expenses:
            if current_sum + cost > max_expense:
                months += 1
                if months > M:
                    return False
                current_sum = cost
            else:
                current_sum += cost
        return True

    left, right = max(expenses), sum(expenses) + 1
    ans = -1
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            ans = mid
            right = mid
        else:
            left = mid + 1
    return ans


N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

print(minMaxMonthlyExpense(N, M, expenses))
