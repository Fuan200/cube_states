import math
from decimal import Decimal, getcontext

# Establece la precisión para Decimal
getcontext().prec = 3000

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

def main():
    cube_size = int(input('Type the value of n: '))
    total_states = states(cube_size)

    rounded_states = round(total_states)
    formatted_states = f'{rounded_states:,}'.replace(',', ' ')
    print(f'Number of possible states in a cube {cube_size}x{cube_size}x{cube_size} = {formatted_states}\n')
    
if __name__ == '__main__':
    main()
