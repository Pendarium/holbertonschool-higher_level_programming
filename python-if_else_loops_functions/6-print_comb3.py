#!/usr/bin/python3

for dizaine in range(0, 9):
    for unité in range(dizaine + 1, 10):
        if dizaine == 8 and unité == 9:
            print("{}{}".format(dizaine, unité))
        else:
            print("{}{}".format(dizaine, unité), end=", ")
