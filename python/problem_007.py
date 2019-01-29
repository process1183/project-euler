#!/usr/bin/env python3
"""
Project Euler - Problem 7
https://projecteuler.net/problem=7

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

PRIME_N = 10001


def main():
    c = 0
    i = 0
    while c < PRIME_N:
        i += 1
        if libeuler.is_prime(i):
            c += 1

    print(i)


if __name__ == "__main__":
    main()
