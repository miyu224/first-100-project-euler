def compute():
    # Math formular solution
    square_of_sum = sum_first_n(100) ** 2
    ans = square_of_sum - sum_square(100)
    return str(ans)


def sum_square(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum_first_n(n):
    return n * (n + 1) / 2


def compute_pure_programming():
    # Pure programming no math required
    square_of_sum = sum(x for x in range(1, 101)) ** 2
    sum_square = sum(x * x for x in range(1, 101))
    ans = square_of_sum - sum_square

    return str(ans)


if __name__ == "__main__":
    print(compute())
    print(compute_pure_programming())
