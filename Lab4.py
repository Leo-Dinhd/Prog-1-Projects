def fibonacci(num1):
    a, b = 0, 1
    for i in range(num1 - 1):
        a, b = b, a + b
    return a

def is_prime(num1):
    if num1 < 2:
        return False
    for j in range(2, num1):
        if num1 % j == 0:
            return False
    return True

def print_prime_factors(num1):
    original = num1
    numbers = []
    divisor = 2
    while num1 >1:
        if num1 % divisor == 0:
            numbers.append(divisor)
            num1 = num1 // divisor
        else:
            divisor +=1

    print(f"original = " + " * ".join(str(f) for f in numbers))