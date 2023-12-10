#!/usr/bin/python3
for num in range(ord('a'), ord('z') + 1):
    if chr(num) != 'e' and chr(num) != 'q':
        print('{:c}'.format(num), end='')
