# def sum_nums(*args):
#     print(args)
#     print(type(args))
#     print(args[0])
#     return sum(args)

# print(sum_nums(4, 6, 8))


# ---------------- arg with key

# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# info = get_posts_info('Bogdan', 25)
# print(info)

# info = get_posts_info(posts_qty= 25, name= 'Reveseal')
# print(info)

# info = get_posts_info('Bogdan', posts_qty= 25)
# print(info)

# -----------------------


# def get_posts_info(**person):
#     print(person)
#     print(type(person))
#     info = (
#         f"{person['name']} wrote "
#         f"{person['posts_qty']} posts"
#     )
#     return info

# info = get_posts_info(name = 'Bogdan', posts_qty = 25)
# print(info)


def get_posts_info(**person):
    print(person)
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info

info = get_posts_info(name = 'Bogdan', posts_qty = 35, id = 987)
print(info)