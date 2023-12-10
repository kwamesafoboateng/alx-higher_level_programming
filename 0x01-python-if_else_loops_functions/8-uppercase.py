#!/usr/bin/python3
def uppercase(str):
    for _case in str:
        if ord(_case) >= 97 and ord(_case) <= 122:
            _case = chr(ord(_case) - 32)
        print("{}".format(_case), end="")
    print()
