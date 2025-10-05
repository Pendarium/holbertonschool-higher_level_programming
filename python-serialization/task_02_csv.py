#!/usr/bin/env python3
"""
This module contains a function that
reads a csv and convert it into a json
"""
import json
import csv


def convert_csv_to_json(csv_source_file):
    """
    Function that read a csv and convert
    it into a json file
    """
    try:
        my_list = []
        with open(csv_source_file, 'r') as source_file:
            csv_dict = csv.DictReader(source_file)
            for element in csv_dict:
                my_list.append(element)
        with open("data.json", 'w') as dest_file:
            json.dump(my_list, dest_file)
        return True
    except Exception:
        return False
