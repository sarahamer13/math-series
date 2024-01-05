"""
This function calculates the nth value in the Fibonacci series
iteratively. If the input n is less than or equal to 0,
it returns 0. If n is 1, it returns 1. Otherwise, it uses a loop
to compute the Fibonacci value by iteratively updating
two variables (a and b) until reaching the desired index n. 
Finally, it returns the calculated Fibonacci value at index n
"""
def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def lucas(n):

    """
This function calculates the nth value in a modified Fibonacci-like series iteratively.
If the input n is equal to 0, it returns 2. If n is 1, it returns 1. 
Otherwise, it uses a loop to compute the series value by iteratively
updating two variables (a and b) until reaching the desired index n. 
Finally, it returns the calculated value at index n.

    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def sum_series(n, first=0, second=1):
    
    """
This function calculates the nth value in a series based on the given parameters
(first and second). If the input n is 0, it returns the value of first.
If n is 1, it returns the value of second.
For n greater than 1, the function uses a loop to
iteratively calculate the series value by updating two variables (a and b)
until reaching the desired index n.
Finally, it returns the calculated value at index n.

    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        a, b = first, second
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
