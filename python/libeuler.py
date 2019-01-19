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


_fibmem = [0, 1]
def nth_fibonacci(n: int) -> int:
    """
    Calculate the Nth number in the Fibonacci sequence.

    https://en.wikipedia.org/wiki/Fibonacci_number
    """
    while n > len(_fibmem)-1:
        _fibmem.append(_fibmem[-2] + _fibmem[-1])
    return _fibmem[n]
