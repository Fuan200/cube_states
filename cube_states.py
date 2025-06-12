import math

def is_even(n):
    return n % 2 == 0

def states(n):
    if (is_even(n)):
        k = n / 2
        result = math.factorial(7) * pow(3 , 6) * pow(math.factorial(24), k * (k - 1)) / pow(math.factorial(4), 6 * (k - 1) ** 2)
        return result
    else:
        k = (n + 1) / 2
        result = math.factorial(8) * pow(3, 7) * pow(2, 10) * math.factorial(12) * pow(math.factorial(24), k * (k - 2)) / pow(math.factorial(4), 6 * (k -1) * (k - 2))
        return result
    
def main():
    cube_size = int(input('Type the value of n: '))
    total_states = states(cube_size)

    rounded_states = round(total_states)
    formatted_states = f'{rounded_states:,}'
    print(f'Number of possible states in a cube {cube_size}x{cube_size}x{cube_size} = {formatted_states}\n')
    
if __name__ == '__main__':
    main()
