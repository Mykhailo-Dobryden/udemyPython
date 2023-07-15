def update_car_info(**car):
    car['is available'] = True
    return car

cars = update_car_info(brand=['BMW'], price=[80])
print(cars)