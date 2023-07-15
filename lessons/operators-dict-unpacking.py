# grey_button = {
#     'width': 200,
#     'text': 'Buy',
#     'color': 'grey'
# }

# red_button = {
#     'color': 'red',
#     ** grey_button,
# }

# print(red_button)

# print(grey_button)

# -------------------------union--dict--


# button_default = {
#     'text': 'OK',
#     'color': 'black',
#     'width': 0,
#     'height': 0,
# }

# button_style = {
#     'color': 'yellow',
#     'width': 200,
#     'height': 300,
# }

# button = {
#     **button_default,
#     **button_style,
# }

# # button = button_default | button_style

# print(button)


# --------------------

dict_one = {
    'color': 'black',
    'size': 40,
    'speed': 120,
}

dict_two = {
    'color': 'white',
    'state': 'second hand',
    'name': 'Karl'
}

dict_three = {
    'is_available': True,
    'accuracy': 'High',
    'level': '0.47'
}

all_dicts = dict_one | dict_two | dict_three

print(all_dicts)
