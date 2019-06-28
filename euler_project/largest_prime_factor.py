# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Наибольший простой делитель
# Простые делители числа 13195 - это 5, 7, 13 и 29.
#
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

from math import sqrt, ceil


def sieve(n):
    actual = ceil(sqrt(n))
    print(actual)

    while actual > 0:
        if actual % 2 != 0 or actual % 3 != 0 or actual % 5 != 0 or actual % 7 != 0:
            if n % actual == 0:
                return actual
        actual -= 1


print('The biggest prime divisor is ', sieve(600851475143))
