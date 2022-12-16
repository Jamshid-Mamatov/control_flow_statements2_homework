def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>=b and a<=c) or (c<=a and a<=b):

        return a
    elif (b>=a and b<=c) or (c<=b and b<=a):

        return b
    elif (c>=b and c<=a) or (a<=c and c<=b):

        return c
