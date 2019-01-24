#!/usr/bin/env python3
"""
Project Euler - Problem 4
https://projecteuler.net/problem=4

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


def main():
    palindrome = 0
    for n1 in range(100, 1000):
        for n2 in range(n1, 1000):
            r = n1 * n2
            if r > palindrome and libeuler.is_palindrome(r):
                palindrome = r
    print(palindrome)


if __name__ == "__main__":
    main()
