user_input_dict = {}

name_key = input('Type \"key\" for name: ')
name_val = input('Type you name: ')
age_key = input('Type \"key\" for age: ')
age_val = input('Type your age: ')
location_key = input('Type \"key\" for location: ')
location_val = input('Type city where are you from: ')



user_input_dict[name_key] = name_val
user_input_dict[age_key] = int(age_val)
user_input_dict[location_key] = location_val

# user_input_dict[input('Type \"key\" for name: ')] = input('Type you name: ')
# user_input_dict[input('Type \"key\" for age: ')] = input('Type your age: ')
# user_input_dict[input('Type \"key\" for location: ')] = input('Type city where are you from: ')

print(user_input_dict)

user_input_dict['weigh'] = 100
user_input_dict['eye color'] = 'brown'

print(user_input_dict)

del user_input_dict[location_key]

print(user_input_dict)
