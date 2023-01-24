def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-2) + fibonacci(n-1)


def main():
    for n in range(2):
        print(f'Fibonacci number when n = {n} is {fibonacci(n)}')

if __name__ == '__main__':
    main()