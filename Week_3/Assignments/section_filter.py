"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage


def main():
    filename = input("Give me a filename ")
    while True:
        try:
            image = SimpleImage(f'Images/{filename}')
            break
        except FileNotFoundError:
            filename = input("Give me a filename again ")
    filtered_image = narok(image, 153)
    image.show()
    filtered_image.show()


""" 
Does not mutate the object, returns a copy
"""


# 1. determine which pixels in image are above the threshold
# 2. run grayscale function on pixels above the threshold to return the average
# 3. function to loop over each pixel in image and see its value
def narok(image, threshold):
    image_copy = SimpleImage.blank(image.width, image.height)

    for new_pixel in image_copy:
        x = new_pixel.x
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)
        if pixel_average(old_pixel) > threshold:
            image_copy.set_pixel(x, y, grayscale(new_pixel, pixel_average(old_pixel)))
        else:
            image_copy.set_pixel(x, y, old_pixel)
    return image_copy


def grayscale(pixel, value):
    # set RGB of this pixel to value (as a grey)
    pixel.red = value
    pixel.green = value
    pixel.blue = value
    return pixel


def pixel_average(pixel):
    return (pixel.red + pixel.blue + pixel.green) // 3


if __name__ == '__main__':
    main()