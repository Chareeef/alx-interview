#!/usr/bin/python3
"""Prime Game :
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number
from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
our task is to determine who the winner of each game is.
"""

# Create an initial Sieve Of Eratosthenes from 0 (for better readability) to 2
Sieve = [False, False, True]

# Memoize initial prime numbers less than or equal to the largest N so far
N = 2
Primes = {2: [2]}

# Define All the primes found so far
MaxPrimes = [2]


def isWinner(x, nums):
    """Determine the winner of the Prime Game between Ben and Maria, where:
        - x: the number of rounds
        - nums: is an array of numbers, each `n` represent the maximum of the
        `index + 1`-th round's set

    Return: name of the player that won the most rounds,
    and if the winner cannot be determined, return None
    """
    pass


def findPrimes(n, useMax):
    """Define, Memoize and Return the primes <= n
    If `useMax` is True, retrieve primes from MaxPrimes,
    and from Sieve otherwise
    """

    global Sieve
    global Primes
    global MaxPrimes

    print(f'For {n}\'s primes, define, Memoize and Return them')

    # Define
    if useMax:
        print('Use MaxPrimes')

        # Retrieve from already found primes stored in MaxPrimes
        n_primes = [num for num in MaxPrimes if num <= n]

    else:
        print('Use Sieve and update MaxPrimes')

        # Retrieve from Sieve
        n_primes = [i for i in range(n + 1) if Sieve[i] is True]

        # Update MaxPrimes
        MaxPrimes = n_primes

    # Memoize
    Primes[n] = n_primes

    # Return
    return n_primes


def sieveOfEratosthenes(n):
    """Return an array of all the prime numbers less than or equal to `n`
    """

    global Sieve
    global N
    global Primes

    # If the current Sieve is sufficiently large
    if n <= N:

        print(f'Sieve large enough for {n}')
        # If the prime <= n were already defined, return them
        n_primes = Primes.get(n)
        if n_primes:
            print(f'{n}\'s primes already defined')
            return n_primes

        # If not: Define, Memoize and Return them
        else:
            return findPrimes(n, True)

    # If n is beyond the current Sieve, expand it
    else:
        print(f'Sieve needs to be expanded for {n}')

        # Append the needed amount of numbers and set them as True
        for _ in range(N, n):
            Sieve.append(True)

        print('Updated length:', len(Sieve))

        # Update N
        N = n

        # Mark the added composite numbers as False
        i = 2
        while i * i <= N:

            # When a prime number is encountred, set its multiples to False
            for m in range(i + i, N + 1, i):
                Sieve[m] = False

            # Increment `i`
            i += 1

        # Define, Memoize and Return the primes <= n
        return findPrimes(n, False)


if __name__ == '__main__':
    print('\tn = 2:')
    print('2 =>', sieveOfEratosthenes(2))
    print('\n\t===\n')

    print('\tn = 10:')
    print('10 =>', sieveOfEratosthenes(10))
    print('\n\t===\n')

    print('\tn = 5:')
    print('5 =>', sieveOfEratosthenes(5))
    print('\n\t===\n')

    print('\tn = 50:')
    print('50 =>', sieveOfEratosthenes(50))
    print('\n\t===\n')

    print('\tn = 10:')
    print('10 =>', sieveOfEratosthenes(10))
    print('\n\t===\n')

    print('\tn = 50:')
    print('50 =>', sieveOfEratosthenes(50))
    print('\n\t===\n')
