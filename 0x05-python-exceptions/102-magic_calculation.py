#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            res += a ** b / j
        except Exception:
            res = b + a
            break
    return res
