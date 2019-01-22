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
