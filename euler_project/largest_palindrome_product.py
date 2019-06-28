# Largest palindrome product
#
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# Наибольшее произведение-палиндром
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
# полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def is_palindrome(n):
    s = str(n)
    l = len(s)
    shift = 0
    if not l % 2 == 0:
        shift = 1
    print(s[:int(l / 2)], s[int(l / 2):], n)
    return s[:int(l/2)] == s[int(l/2)+shift:][::-1]


def get_largest_palindrome(a=999, b=999):
    i = b
    while a > 99:
        while i > 99:
            if is_palindrome(a * i):
                return a * i
            i -= 1
        i = b
        a -= 1
    return None


print('The largest palindrome is: ', get_largest_palindrome(999, 999))
