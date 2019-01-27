#!/usr/bin/env python3
"""
Project Euler - Problem 6
https://projecteuler.net/problem=6

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
UPPER_LIMIT = 100


def main():
    sum_of_squares = sum([i**2 for i in range(1, UPPER_LIMIT+1)])
    square_of_sums = sum(range(1, UPPER_LIMIT+1))**2
    result = square_of_sums - sum_of_squares
    print(result)


if __name__ == "__main__":
    main()
