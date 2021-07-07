"""
This program creates an image of a set size and assigns
each pixel a random color.
"""

from simpleimage import SimpleImage
import random

RANDOM_MIN = 0
RANDOM_MAX = 255


def main():
    image = create_random()
    image.show()


def create_random():
    """
    Function that creates a 90x90 pixel image and then
    writes random colors to each pixel
    :return: image
    """
    image = SimpleImage.blank(90, 90)
    for pixel in image:
        x = pixel.x
        y = pixel.y
        pixel.red = random.randint(RANDOM_MIN, RANDOM_MAX)
        pixel.green = random.randint(RANDOM_MIN, RANDOM_MAX)
        pixel.blue = random.randint(RANDOM_MIN, RANDOM_MAX)
        image.set_pixel(x, y, pixel)
    return image


if __name__ == '__main__':
    main()
