#!/usr/bin/python3 -i
"""
Helper script for manipulating test data JSON.
"""
import json

DEFAULT_FILENAME = "libeuler_test_data.json"


def load(filename=DEFAULT_FILENAME) -> dict:
    """Return decoded JSON from filename"""
    with open(filename, "r") as inf:
        return json.load(inf)


def save(test_data, filename=DEFAULT_FILENAME):
    """Encode test_data as JSON and write to filename"""
    with open(filename, "w") as outf:
        # write each json object member on its own line
        outf.write("{\n")
        json_items = []
        for k, v in sorted(test_data.items()):
            json_str = json.dumps(v, sort_keys=True)
            json_items.append("\"{}\": {}".format(k, json_str))
        outf.write(",\n".join(json_items))
        outf.write("\n}\n")


if __name__ == "__main__":
    data = load()
    print("JSON data loaded into variable 'data'")
    print("data.keys() = {}\n".format(sorted(data.keys())))
    print("Functions:")
    print("    load(filename={}) -> dict".format(DEFAULT_FILENAME))
    print("    save(test_data, filename={})".format(DEFAULT_FILENAME))
    print()
