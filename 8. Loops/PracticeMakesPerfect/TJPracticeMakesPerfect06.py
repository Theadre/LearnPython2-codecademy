
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x- 1):
            if x % n == 0:
                return False
        return True


print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(6))  # False
print(is_prime(14))  # False
