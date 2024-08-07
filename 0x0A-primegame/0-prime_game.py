#!/usr/bin/python3
"""
Prime Game Simulation
"""


def isWinner(x, nums):
    """Defining the main object."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    results = []
    for n in nums:
        if n == 1:
            results.append('Ben')
            continue

        available = [True] * (n + 1)
        turn = 0
        while True:
            move_made = False
            for num in range(2, n + 1):
                if is_prime[num] and available[num]:
                    for multiple in range(num, n + 1, num):
                        available[multiple] = False
                    move_made = True
                    break

            if not move_made:
                results.append('Ben' if turn == 0 else 'Maria')
                break

            turn = 1 - turn

    maria_wins = results.count('Maria')
    ben_wins = results.count('Ben')

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
