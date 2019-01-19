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


if __name__ == "__main__":
    unittest.main(verbosity=2)
