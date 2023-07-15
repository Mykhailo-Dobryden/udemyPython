a = 5


def my_fn():
    a = 345

    def inner_fn():
        print(a)
    inner_fn()


my_fn()
