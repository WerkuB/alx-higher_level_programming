#!/usr/bin/python3
"""task 2 module"""


def append_write(filename="", text=""):
    """append a string to  file """
    with open(filename, mode='a', encoding='utf-8') as f:
        nb_chars = f.write(text)

    return nb_chars
