"""
Recursion is a programming and mathematical concept where a function or a 
process calls itself to solve a problem or perform a task. In essence, 
it's a way to solve complex problems by breaking them down into smaller, 
more manageable subproblems, often of the same type as the original problem. Recursion relies on two fundamental components:

Base Case: This is a condition that specifies when the recursion should stop. 
It provides a terminating point for the recursive calls, preventing infinite recursion.

Recursive Case: In this part of the function, it calls itself with modified arguments to 
work on a smaller instance of the same problem. The recursive call should eventually lead to the base case.
"""



"""
Factorial Calculation:
The factorial of a non-negative integer n (denoted as n!) is 
the product of all positive integers from 1 to n. Recursion is commonly used to compute factorials.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Fibonacci Sequence:
The Fibonacci sequence is a series of numbers where each number is 
the sum of the two preceding ones. Recursion can be used to calculate Fibonacci numbers.
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
