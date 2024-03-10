def factorial(number):
    value = 1

    for i in range(number):
        value += value * i

    return value

print(factorial(5))