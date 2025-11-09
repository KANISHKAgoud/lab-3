# Non-Recursive (Iterative) Fibonacci with Series and Step Count
def fibonacci_iterative(n):
    fib_series = []
    steps = 0

    a, b = 0, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
        steps += 1

    return fib_series, steps


# Recursive Fibonacci with Series and Step Count
def fibonacci_recursive_series(n, series=None, steps=0):
    if series is None:
        series = [0, 1] if n > 1 else [0]

    # Helper function for recursion
    def helper(a, b, count, steps, series):
        steps += 1
        if count == n:
            return series, steps
        series.append(a + b)
        return helper(b, a + b, count + 1, steps, series)

    if n == 0:
        return [0], steps
    elif n == 1:
        return [0], steps
    else:
        return helper(0, 1, 2, steps, series)


# ---- Main Program ----
n = int(input("Enter the Fibonacci term to calculate: "))

# Iterative method
fib_series_iter, steps_iter = fibonacci_iterative(n)
print("\n--- Non-Recursive (Iterative) Method ---")
print("Iterative Fibonacci series:", fib_series_iter)
print("Fibonacci number =", fib_series_iter[-1] if fib_series_iter else 0)
print("Total steps taken =", steps_iter)

# Recursive method
fib_series_rec, steps_rec = fibonacci_recursive_series(n)
print("\n--- Recursive Method ---")
print("Recursive Fibonacci series:", fib_series_rec)
print("Fibonacci number =", fib_series_rec[-1] if fib_series_rec else 0)
print("Total steps taken =", steps_rec)

# ---- Time & Space Complexity ----
"""
Iterative:
    Time Complexity: O(n)
    Space Complexity: O(n)

Recursive:
    Time Complexity: O(2^n)  [if pure recursion without series building]
    Space Complexity: O(n)
"""
