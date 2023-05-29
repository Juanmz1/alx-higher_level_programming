#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: ", e, file=stderr)
    finally:
        return result
