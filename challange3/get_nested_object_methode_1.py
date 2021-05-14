#!/usr/bin/env python3


from functools import reduce
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
object = {'a':{'b':{'c':'d'}}}
print (deep_get(object, "a.b.c"))

