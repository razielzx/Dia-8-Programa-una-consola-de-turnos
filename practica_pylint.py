"""This is just a practice of the pylint library"""

def sum_two_int(n1, n2):
    """
    Function to sum
        args:
            int n1: the first integer
            int n2: the second integer
    """
    return n1 + n2

result = sum_two_int(5,7) #pylint: disable=invalid-name

print(result)
