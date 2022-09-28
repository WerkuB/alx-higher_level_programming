#!/usr/bin/python3
"""Task 0 file IO"""


def read_file(filename=""):
    """ A func which print the content of utf-8 encoding file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
