#!/usr/bin/python3
"""
This module contains a program that
calls a list from a specific json file,
append it, and the updates made.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json") is False:
    list = []
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])
    save_to_json_file(list, "add_item.json")

else:
    list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])
    save_to_json_file(list, "add_item.json")
