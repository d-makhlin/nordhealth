from typing import List

from nord_health_solution import NordHealthSolution


if __name__ == '__main__':
    while True:
        try:
            numbers: List[int] = [int(n) for n in input('Enter numbers separated by space: ').split(' ')]
        except ValueError:
            print('Entered numbers should be integers!')
            continue
        except KeyboardInterrupt:
            break
        NordHealthSolution.to_print(numbers)
