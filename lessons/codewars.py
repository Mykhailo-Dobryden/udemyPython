def is_square(n):
    sq_root = n ** 0.5
    if n == sq_root ** 2:
        return True
    else:
        return False


print(is_square(-2))
