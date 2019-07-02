def first_n_fibba(n, prev_1, prev):
    if n > 0:
        now = prev + prev_1
        print(now)
        first_n_fibba(n - 1, prev, now)
    else:
        return


def fib(n):
    print(0)
    print(1)
    first_n_fibba(n - 2, 0, 1)


if __name__ == "__main__":
    fib(5)
