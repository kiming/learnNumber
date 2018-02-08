import math

x = 12

def nature(input):
    sum = 0
    for index in range(input):
        sum += input ** index / math.factorial(index)
    return sum

print(nature(0))
