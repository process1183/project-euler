#!/usr/bin/env python3
"""
Project Euler - Problem 5
https://projecteuler.net/problem=5

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
import functools

import libeuler

UPPER_LIMIT = 20


def get_list(ulimit: int) -> list:
    l = list(range(1,ulimit+1))
    l.reverse()
    s = set(l)
    for i in l:
        if i not in s:
            continue
        f = set(libeuler.factor(i))
        f.remove(i)
        s -= f
    return list(s)


def main():
    nl = get_list(UPPER_LIMIT)
    res = functools.reduce(libeuler.lcm, nl)
    print(res)


if __name__ == "__main__":
    main()
