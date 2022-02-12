# Generator for the Fibonacci sequence
def fibonacci_generator():
    prev = 0
    next = 0

    while True:
        if next == 0:
            yield 0
            next += 1
        else:
            yield next
            temp = next
            next = prev + next
            prev = temp


def is_fib(num):
    if num < 0:
        raise Exception('Negative numbers are not in the Fibonacci sequence')
    else:
        for fibonacci_number in fibonacci_generator():
            if fibonacci_number == num:
                return True
            elif fibonacci_number < num:
                continue
            else:
                return False


num = 200

print(is_fib(num))
