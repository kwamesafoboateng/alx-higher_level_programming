#!/usr/bin/python3
def add_arg(argv):
    b = len(argv) - 1
    if b == 0:
        print("{:d}".format(b))
        return
    else:
        a = 1
        add = 0
        while a <= b:
            add += int(argv[a])
            a += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
