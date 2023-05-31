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
    for i in range(2, 9):
        number = states(i)
        uwu = "{:.0f}".format(number)
        uwu = int(uwu)
        owo = "{:,}".format(uwu)
        print(f'Number of possible states in a cube {i}x{i}x{i} = {owo}\n')
    
if __name__ == '__main__':
    main()