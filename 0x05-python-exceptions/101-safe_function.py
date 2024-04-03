#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as j:
        sys.stderr.write("Exception: {}\n".format(j))
        res = None
    return (res)
