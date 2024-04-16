#!/usr/bin/python3
""" write an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file writes an Object to a text file
    using a json representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
