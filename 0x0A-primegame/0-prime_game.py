#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n using the
    Sieve of Eratosthenes.
    Args:
        max_n (int): The upper boundary for prime generation.
    Returns:
        List[int]: A list of prime numbers up to max_n.
    """
    if max_n < 2:
        return []
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on multiple rounds.
    Args:
        x (int): Number of rounds.
        nums (List[int]): Upper limits of ranges for each round.
    Returns:
        str: Name of the player who won the most rounds ('Maria' or 'Ben'), or None if a tie.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_list = sieve_of_eratosthenes(max_n)

    maria_wins = ben_wins = 0

    for n in nums:
        prime_count = len([p for p in prime_list if p <= n])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
