def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n0=n%10
    n//=10
    n1=n%10
    n//=10
    n2=n%10
    n//=10
    n3=n%10
    n4=n//10

    if n0>=n1 and n0>=n2 and n0>=n3 and n0>=n4:
        return n0
    elif n1>=n0 and n1>=n2 and n1>=n3 and n1>=n4:
        return n1
    elif n2>=n1 and n2>=n0 and n2>=n3 and n2>=n4:
        return n2
    elif n3>=n1 and n3>=n2 and n3>=n0 and n3>=n4:
        return n3
    else:
        return n4
