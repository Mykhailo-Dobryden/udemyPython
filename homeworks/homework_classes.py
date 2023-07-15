class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def change_title(self, new_title):
        self.title = new_title

    def __str__(self):
        return f"{self.title}.{self.extension}"


flowers = Image('1920x1080', 'Flower', 'jpg')
car = Image('760x430', 'BMW', 'png')
bus = Image('1760x1430', 'MAN', 'jpeg')

print(bus.resolution)
bus.resize('1920x1080')
print(bus.resolution)

print(bus)

