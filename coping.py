from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great course!')
info_deepcopy['reviews'].append('Super!')

print(info)

print(info_deepcopy)