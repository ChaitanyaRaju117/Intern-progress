# Day 2 - Prime Checker

def is_prime(n):
    """
    Checks if a given number is prime.
    Returns True if prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_primes_upto(limit):
    """Prints all prime numbers from 2 to limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    print(f"Prime numbers up to {limit}: {primes}")


print("Testing individual numbers:")
test_numbers = [1, 2, 3, 4, 13, 17, 20, 97]
for num in test_numbers:
    result = is_prime(num)
    print(f"  is_prime({num}) → {result}")

print()
print_primes_upto(50)