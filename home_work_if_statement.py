def get_distance_info(**info):
    if ('distance' in info) and type(info["distance"]) == int:
        return f"Distance to your destination is {info['distance']}"

    if ('speed' in info) and ('time' in info):
        return f"Distance to you destination is {info['speed'] * info['time']}"

    return "No distance info is available"


to_odessa = {
    'city': 'Odessa',
    'distance': 1200,
    'speed': 60,
    'time': 3,
}

to_kyiv = {
    'city': 'Kyiv',
    'speed': 80,
    'time': 6,
}

print(get_distance_info(**to_odessa))
print(get_distance_info(**to_kyiv))
