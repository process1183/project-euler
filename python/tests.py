#!/usr/bin/env python3
"""
libeuler tests

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
import json
import os
import unittest

import libeuler

JSON_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "libeuler_test_data.json")


def get_test_data(filename: str) -> dict:
    with open(filename, "r") as inf:
        data = inf.read()
    return json.loads(data)


class TestLibeuler(unittest.TestCase):
    _answers = get_test_data(JSON_FILE)

    def test_fibonacci(self):
        for i, v in enumerate(self._answers["fibonacci"]):
            self.assertEqual(libeuler.nth_fibonacci(i), v)

    def test_primes(self):
        prime_list = self._answers["primes"]
        computed = []
        for i in range(0, prime_list[-1]+1):
            if libeuler.is_prime(i):
                computed.append(i)
        self.assertListEqual(computed, prime_list)

        for n in self._answers["primes_random"]:
            self.assertEqual(libeuler.is_prime(n), True)

    def test_prime_factors(self):
        for n in self._answers["primes"]:
            self.assertListEqual(libeuler.prime_factor(n), [n])

        for k, v in self._answers["prime_factors"].items():
            k = int(k) # JSON keys are strings
            self.assertListEqual(libeuler.prime_factor(k), v)

    def test_reversed_ints(self):
        for n, rn in self._answers["reversed_ints"]:
            self.assertEqual(libeuler.reverse_int(n), rn)

    def test_palindromes(self):
        l = []
        for i in range(0, self._answers["palindromes"][-1]+1):
            if libeuler.is_palindrome(i):
                l.append(i)
        self.assertListEqual(l, self._answers["palindromes"])

    def test_factors(self):
        for n in self._answers["primes"]:
            self.assertListEqual(libeuler.factor(n), [1, n])

        for k, v in self._answers["factors"].items():
            k = int(k) # JSON keys are strings
            self.assertListEqual(libeuler.factor(k), v)


if __name__ == "__main__":
    unittest.main(verbosity=2)
