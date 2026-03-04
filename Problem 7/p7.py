import math


def is_prime(n) -> bool:
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def compute():
    ans = 3
    count = 2

    while count < 10001:
        ans += 2
        if is_prime(ans):
            count += 1

    return str(ans)


if __name__ == "__main__":
    print(compute())
