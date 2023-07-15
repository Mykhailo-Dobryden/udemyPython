def image_info(img):
    if ('image_title' not in img) or ('image_id' not in img):
        raise TypeError("There is no image_title or image_id")
    return f"Image {img['image_title']} has id {img['image_id']}"


print(image_info({'image_id': 34, 'image_title': 'Cat'}))

try:
    print(image_info({'image_id': 82}))
except TypeError as e:
    print(e)
