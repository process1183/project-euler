#!/usr/bin/env python3
"""
Project Euler - Problem 9
https://projecteuler.net/problem=9

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


def main():
    for a in range(1, 500):
        for b in range(a, 500):
            c = 1000 - b - a
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return


if __name__ == "__main__":
    main()
