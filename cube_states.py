import sys
sys.set_int_max_str_digits(10_000)

import math
from decimal import Decimal, getcontext

getcontext().prec = 5000

def is_even(n):
    return n % 2 == 0

def states(n):
    if is_even(n):
        k = Decimal(n) / 2
        result = Decimal(math.factorial(7)) * Decimal(3) ** 6 * Decimal(math.factorial(24)) ** (k * (k - 1)) / Decimal(math.factorial(4)) ** (6 * (k - 1) ** 2)
        return result
    else:
        k = Decimal(n + 1) / 2
        result = Decimal(math.factorial(8)) * Decimal(3) ** 7 * Decimal(2) ** 10 * Decimal(math.factorial(12)) * Decimal(math.factorial(24)) ** (k * (k - 2)) / Decimal(math.factorial(4)) ** (6 * (k - 1) * (k - 2))
        return result
    
def to_scientific_notation(n, digits=3):
    n_str = str(n)
    exponent = len(n_str) - 1
    if len(n_str) > digits + 1:
        mantissa = n_str[0] + '.' + n_str[1:digits+1]
    else:
        mantissa = n_str
        exponent = 0
    return f"{mantissa}e+{exponent}"

def main():
    cube_size = int(input('Type the value of n: '))
    total_states = states(cube_size)

    rounded_states = round(total_states)

    if cube_size >= 6:
        formatted_states = to_scientific_notation(rounded_states, digits=3)
    else:
        formatted_states = f'{rounded_states:,}'.replace(',', ' ')

    print(f'Number of possible states in a cube {cube_size}x{cube_size}x{cube_size} = {formatted_states}\n')
    
if __name__ == '__main__':
    main()
