#!/usr/bin/env python3
"""
Project Euler Algorithms
Copyright (C) 2019  Josh Gadeken

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#pylint: disable=invalid-name
import functools
import math


_fibmem = [0, 1]
def nth_fibonacci(n: int) -> int:
    """
    Calculate the Nth number in the Fibonacci sequence.

    https://en.wikipedia.org/wiki/Fibonacci_number
    """
    while n > len(_fibmem)-1:
        _fibmem.append(_fibmem[-2] + _fibmem[-1])
    return _fibmem[n]


@functools.lru_cache(maxsize=None, typed=False)
def is_prime(n: int) -> bool:
    """
    Test if `n` is a prime number.

    https://en.wikipedia.org/wiki/Prime_number
    """
    if n in (0, 1):
        return False
    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    y = 3
    upper_limit = int(math.sqrt(n)) + 1

    while y < upper_limit:
        if n % y == 0:
            return False
        else:
            y += 2 # skip even numbers

    return True


def prime_factor(n: int) -> list:
    """
    Calculate the prime factors for a number.

    https://en.wikipedia.org/wiki/Prime_factor
    """
    prime_factors = []
    y = 2

    while y <= n:
        if is_prime(y):
            # if y is prime and y goes into n evenly, y is a prime factor
            if n % y == 0:
                prime_factors.append(y)
                # set n to the counterpart multiplier of y; used to continue prime factorization
                n = n / y
                y = 1
        y += 1

    return sorted(prime_factors)


def reverse_int(n: int) -> int:
    """
    Reverse digits in an integer.
    """
    return int(str(n)[::-1])


def is_palindrome(n: int) -> bool:
    """
    Test if a number is palindromic.

    https://en.wikipedia.org/wiki/Palindromic_number
    """
    return n == reverse_int(n)


def factor(n: int) -> list:
    """
    Calculate the factors for a number.

    https://en.wikipedia.org/wiki/Factorization
    """
    if n == 0:
        return []

    factors = [1, n]
    y = 2
    upper_limit = int(math.sqrt(n))

    while y <= upper_limit:
        if n % y == 0:
            factors.append(y)
            factors.append(n//y)
        y += 1

    return sorted(list(set(factors)))


def lcm(a: int, b: int) -> int:
    """
    Compute the Least common multiple for `a` and `b`.

    https://en.wikipedia.org/wiki/Least_common_multiple
    """
    if a == 0 and b == 0:
        return 0

    return (a // math.gcd(a, b)) * b


def sliding_window(lst: list, wsize: int) -> iter:
    """
    Iterate over overlapping subslices of length `wsize`.
    """
    if wsize >= len(lst):
        yield lst
        return

    ws = 0
    we = wsize

    while we <= len(lst):
        yield lst[ws:we]
        ws += 1
        we += 1


def sieve_of_eratosthenes(limit: int) -> iter:
    """
    Generate prime numbers up to `limit`.
    """
    l = [True for i in range(limit)]
    l[0] = False
    l[1] = False

    for i, prime in enumerate(l):
        if prime:
            for n in range(i**2, limit, i):
                l[n] = False
            yield i


def ap_term_count(first_term: int, last_term: int, common_diff: int) -> int:
    """Calculate the number of terms in a finite arithmetic progression.

    https://en.wikipedia.org/wiki/Arithmetic_progression

    Args:
        first_term: The first number in the arithmetic progression
        last_term: The last number in the arithmetic progression
        common_diff: The difference between consecutive terms

    Returns:
        The number of terms in the finite arithmetic progression.
    """
    return ((last_term - first_term) // common_diff) + 1


def arithmetic_series(n_terms: int, first_term: int, last_term: int) -> int:
    """Calculate the sum of the members of a finite arithmetic progression.

    https://en.wikipedia.org/wiki/Arithmetic_progression

    Args:
        n_terms: Number of terms in the arithmetic progression
        first_term: The first number in the arithmetic progression
        last_term: The last number in the arithmetic progression

    Returns:
        The sum of the arithmetic progression
    """
    return (n_terms * (first_term + last_term)) // 2
