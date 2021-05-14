#!/usr/bin/env python3

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

all_keys = {'a':{'b':{'c':{'d':'e'}}}}

for key, value in recursive_items(all_keys):
    print(value)
