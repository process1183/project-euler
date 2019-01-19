#!/usr/bin/env python3
"""
Project Euler - Problem 2
https://projecteuler.net/problem=2

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
    i = 0
    f = 0
    s = 0

    while f < 4000000:
        f = libeuler.nth_fibonacci(i)
        if f % 2 == 0:
            s += f
        i += 1

    print(s)


if __name__ == "__main__":
    main()
