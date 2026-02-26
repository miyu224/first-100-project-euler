import math


def prime_factorization(n):
    """Return prime factorization as a dictionary {prime: power}"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def compute():
    # Prime factorize all numbers from 1 to 20
    max_factors = {}

    for num in range(1, 21):
        factors = prime_factorization(num)
        # Keep track of the maximum power for each prime factor
        for prime, power in factors.items():
            max_factors[prime] = max(max_factors.get(prime, 0), power)

    # Multiply all factors with their maximum powers
    result = 1
    for prime, power in max_factors.items():
        result *= prime**power

    return str(result)


def lcm_way():
    ans = math.lcm(*range(1, 21))  # just use built in function
    return str(ans)


def math_way():
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]  # all prime < k = 20
    MAX_POWER = [1] * len(PRIMES)
    k = 20
    ans = 1

    for i in range(0, len(PRIMES)):
        if PRIMES[i] <= math.sqrt(k):
            MAX_POWER[i] = math.floor(math.log(k) / math.log(PRIMES[i]))
        ans *= PRIMES[i] ** MAX_POWER[i]

    return str(ans)


if __name__ == "__main__":
    print(compute())
    print(lcm_way())
    print(math_way())
