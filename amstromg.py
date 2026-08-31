def is_armstrong(n):
    digits = str(n)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == n


print(is_armstrong(153))