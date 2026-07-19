def rep(n):
    if (n == 0):
        return
    rep(n-1)
    print(f"day {n}")


def ft_count_harvest_recursive():
    day = int(input("Days until harvest:"))
    rep(day)
    print("Harvest time!")
