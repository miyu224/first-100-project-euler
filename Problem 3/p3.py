# Trial division -> suitable for about 10^12
# Combine Eratosthenes sieves for reduce number to test (find all prime number that <= sqrt(n))


def compute(n):
    # max_factor stores the largest prime factor found so far
    # Invariant: before testing i, all prime factors < i
    # have already been removed from n
    max_factor = 1

    # Remove all factors of 2 (the only even prime)
    # After this, n is odd
    while n % 2 == 0:
        max_factor = 2
        n //= 2

    # Test odd divisors starting from 3
    i = 3

    # We only need to check while i*i < n:
    # If n is composite, it must have a divisor <= sqrt(n).
    # If none is found up to sqrt(n), n must be prime.
    while i * i < n:

        # If i divides n, remove all copies of i.
        # i must be prime here, because any smaller prime factors were already removed.
        while n % i == 0:
            max_factor = i
            n //= i

        i += 2  # skip even numbers

    # If n > 1 here, then n has no divisor <= sqrt(n),
    # so n itself is prime and is the largest factor.
    if n > 1:
        max_factor = n

    return str(max_factor)


if __name__ == "__main__":
    print(compute(n=600851475143))
