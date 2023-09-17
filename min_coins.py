# given a set of coin {c1, c2, ... ,cn} and a target sum of money m
# what is the minimum number of coins that form the sum m


def min_ignore_none(a, b):
    if a is not None and b is not None:
        return min(a, b)
    if a is None:
        return b
    if b is None:
        return a
    return None


memo = {}

def min_coins(m, coins):
    if m in memo:
        return m
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            if m - coin >= 0:
                answer = min_ignore_none(answer, min_coins(m - coin, coins) + 1)
    memo[m] = answer
    return answer

def min_coins_bottom_up(m, coins):
    memo[0] = 0
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue

            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)

    return memo[m]

def ways_to_get_sum(m, coins):
    if m in memo:
        return memo[m]
    if m == 0:
        answer = 1
    else:
        r = 0
        for c in coins:
            t = m - c
            if t >= 0:
                r += ways_to_get_sum(t, coins)
        answer = r
    memo[m] = answer
    return answer

def ways_to_get_sum_bottom_up(m, coins):
    memo = {}
    for i in range(0, m+1):
        memo[i] = 0
    for i in range(1, m+1):
        r = 0
        for c in coins:
            t = i - c

            if t == 0:
                memo[i] += 1

            if t >= 0:
                r += memo[t]

        memo[i] += r
        
    return memo[m]

def maze_problem(grid_size):
    # a rabbit starts on the top left and can only go right or down
    # he must arrive at the bottom right
    pass

"""
re-learning dynamic programming following this nice video
https://www.youtube.com/watch?v=Hdr64lKQ3e4
"""
#print(ways_to_get_sum_bottom_up(87, [1, 4, 5, 8]))
grid_size = (10, 10)