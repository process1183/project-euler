#!/usr/bin/env python3
"""
Project Euler - Problem 1
https://projecteuler.net/problem=1

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
import libeuler

UPPER_LIMIT = 1000



def sum_of_multiples(n: int, limit: int) -> int:
    """Calculate the sum of the multiples of `n` up to `limit`"""
    last_term = n * (limit // n)
    n_terms = libeuler.ap_term_count(n, last_term, n)
    ap_sum = libeuler.arithmetic_series(n_terms, n, last_term)

    return ap_sum


def main() -> None:
    # Range limit is non-inclusive
    limit = UPPER_LIMIT - 1

    threes = sum_of_multiples(3, limit)
    fives = sum_of_multiples(5, limit)

    # Inclusion-exclusion principle: the sum of the multiples of 15
    # is included in both the sum of the multiples of 3 and the sum
    # of the multiples of 5- so remove the duplication.
    fifteens = sum_of_multiples(15, limit)
    s = threes + fives - fifteens

    print(s)



if __name__ == "__main__":
    main()
