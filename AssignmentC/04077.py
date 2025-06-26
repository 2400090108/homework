def count_sequences(n):
    def dfs(push_num, stack, popped):
        nonlocal count
        if popped == n:
            count += 1
            return
        if push_num <= n:
            stack.append(push_num)
            dfs(push_num +1, stack, popped)
            stack.pop()
        if stack:
            top = stack.pop()
            dfs(push_num, stack, popped + 1)
            stack.append(top)

    count = 0
    dfs(1, [], 0)
    return count

n = int(input())
print(count_sequences(n))