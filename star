#!/usr/bin/env python3

import colors as c

import time

print(c.clear)

try:
    while True:
        print('/')
        time.sleep(.15)
        print(c.clear)
        print('-')
        time.sleep(.15)
        print(c.clear)
        print('\\')
except KeyboardInterrupt:
    print(c.clear)
    exit()
