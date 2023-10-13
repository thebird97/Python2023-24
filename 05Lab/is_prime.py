def is_prime(n):
    """Return True if n is a prime number, else False."""
    # Check if n is less than 2 (as prime numbers are greater than 1)
    if n < 2:
        return False
    # Check for factors of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(9))