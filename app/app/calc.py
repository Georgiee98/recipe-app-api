"""Calculator functions"""


def add(x,y):
    """Add x and y and return results"""
    return x + y

def substract(x,y):
    """Substract x from y and return results."""
    res = 0
    if x > y:
        res = x - y
    else:
        res = y - x
    return res