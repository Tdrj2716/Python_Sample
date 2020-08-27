# Fibonacci numbers module

def fibonacci(n: int) -> int:
    p, q = 0, 1 # assign multiple values to multiple variables
    for i in range(n - 1):
        p, q = q, p+q
    return q

if __name__ == "__main__":
    for i in range(1, 6):
        print(fibonacci(i))