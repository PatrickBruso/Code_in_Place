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
    blue_image = create_blue()
    image.show()
    blue_image.show()

    #for i in range((image.height + image.width // 2) // 9):
        # nested loops?


def create_blue():
    """
    Function that creates a 90x90 image that is blue
    :return: image
    """
    image = SimpleImage.blank(90, 90)
    for pixel in image:
        x = pixel.x
        y = pixel.y
        pixel.red = 0
        pixel.green = 0
        pixel.blue = 255
        image.set_pixel(x, y, pixel)
    return image


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


def pixel_average(pixel):
    # determine average of pixel to check against threshold
    return (pixel.red + pixel.blue + pixel.green) // 3


if __name__ == '__main__':
    main()
