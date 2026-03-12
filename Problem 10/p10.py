def compute():
    ans = 0
    n = 2000000
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    i = 2

    while i * i < n:
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1

    ans = sum(i for i in range(2, n) if is_prime[i])

    return str(ans)


if __name__ == "__main__":
    print(compute())
