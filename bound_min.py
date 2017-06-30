
def bound_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in ((first, ) + args):
         if arg < res and lo < arg < hi:
             res = arg
    return max(res, lo)

print(bound_min(-5, 12, 13, lo=0, hi=255))
