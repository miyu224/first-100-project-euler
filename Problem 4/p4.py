def compute():
    ans = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            product = str(a * b)
            if product == product[::-1]:
                ans = max(ans, int(product))

    return str(ans)


if __name__ == "__main__":
    print(compute())
