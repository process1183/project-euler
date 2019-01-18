#!/usr/bin/python3 -i
"""
Helper script for manipulating test data JSON.
"""
import json

DEFAULT_FILENAME = "libeuler_test_data.json"


def load(filename=DEFAULT_FILENAME) -> dict:
    """Return decoded JSON from filename"""
    with open(filename, "r") as inf:
        return json.loads(inf.read())


def save(test_data, filename=DEFAULT_FILENAME):
    """Encode test_data as JSON and write to filename"""
    with open(filename, "w") as outf:
        outf.write(json.dumps(test_data, sort_keys=True))


if __name__ == "__main__":
    #pylint: disable=invalid-name
    data = load()
    print("JSON data loaded into variable 'data'")
    print("data.keys() = {}\n".format(sorted(data.keys())))
    print("Functions:")
    print("    load(filename={}) -> dict".format(DEFAULT_FILENAME))
    print("    save(test_data, filename={})".format(DEFAULT_FILENAME))
    print()
