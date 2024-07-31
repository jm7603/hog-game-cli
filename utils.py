import math
import os
import platform


def clear_and_move_cursor():
    if platform.system() == "Windows":
        if platform.release().startswith('10') or platform.release().startswith('11'):
            print("\033[2J\033[0;0f", end="")
        else:
            os.system('cls')
    else:
        print("\033[2J\033[0;0f", end="")


def factor_count(n: int) -> int:
    if n <= 0:
        return 0

    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1

    return count


def is_prime(n: int) -> bool:
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    i = 3
    h = math.floor(math.sqrt(n))
    while i <= h:
        if n % i == 0:
            return False
        i += 1

    return True


def next_prime(n: int) -> int:
    t = n + 1
    while not is_prime(t):
        t += 1

    return t
