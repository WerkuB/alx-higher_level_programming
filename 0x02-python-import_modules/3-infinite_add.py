#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    inf_add = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            inf_add += int(arg)
    print(inf_add)
