#!/usr/bin/python3
"""Prime Game (Rules are explained in the README)
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
        - nums: an array of numbers, each `n` represent the maximum of the
        `index + 1`-th round's set

    Return: name of the player that won the most rounds,
    and if the winner cannot be determined, return None
    """

    def getPrimes(n, useMax):
        """Define, Memoize and Return the primes <= n
        If `useMax` is True, retrieve primes from MaxPrimes,
        and from Sieve otherwise
        """

        global Sieve
        global Primes
        global MaxPrimes

        # Define
        if useMax:

            # Retrieve from already found primes stored in MaxPrimes
            n_primes = [num for num in MaxPrimes if num <= n]

        else:

            # Retrieve from Sieve
            n_primes = [i for i in range(n + 1) if Sieve[i] is True]

            # Update MaxPrimes
            MaxPrimes = n_primes

        # Memoize
        Primes[n] = n_primes

        # Return
        return n_primes

    def findPrimes(n):
        """Return an array of all the prime numbers less than or equal to `n`
        """

        global Sieve
        global N
        global Primes

        # If the current Sieve is sufficiently large
        if n <= N:

            # If the prime <= n were already defined, return them
            n_primes = Primes.get(n)
            if n_primes:
                return n_primes

            # If not: Define, Memoize and Return them
            else:
                return getPrimes(n, True)

        # If n is beyond the current Sieve, expand it
        else:

            # Append the needed amount of numbers and set them as True
            for _ in range(N, n):
                Sieve.append(True)

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
            return getPrimes(n, False)

    # Initialize scores
    Maria = 0
    Ben = 0

    # Play rounds
    for i in range(x):

        # Compute availabe prime numbers for this round
        primes = findPrimes(nums[i])

        # Since Maria always begin, if the number of availabe primes
        # is odd, she wins the round, otherwise, Ben wins
        if len(primes) % 2 != 0:
            Maria += 1
        else:
            Ben += 1

    # Return None if it is a draw, otherwise return th winner's name
    if Maria == Ben:
        return None
    else:
        return 'Maria' if Maria > Ben else 'Ben'
