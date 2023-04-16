def fibonacciRecursive(num):
    if num <= 1:
        return num
    return fibonacciRecursive(num - 2) + fibonacciRecursive(num - 1)

if __name__ == '__main__':
    pass