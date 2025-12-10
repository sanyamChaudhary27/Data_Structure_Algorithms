##    check_palindrome

def generate_fib(size):
    if size <= 0:
        return []
    fib = [0, 1]
    for _ in range(2, size):
        fib.append(fib[-1] + fib[-2])
    return fib[:size]

def check_fib_prefix(lst):
    fib = generate_fib(len(lst))
    return lst == fib

print(check_fib_prefix([0, 1, 1, 2, 3, 5]))
