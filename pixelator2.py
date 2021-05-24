"""
Program that takes in an image and assigns a color from a palette to each pixel
and returns a copy of the new image
"""

from simpleimage import SimpleImage
import math


def main():
    """
    filename = input("Give me a filename ")
    while True:
        try:
            image = SimpleImage(f'images/{filename}')
            break
        except FileNotFoundError:
            filename = input("Give me a filename again ")
    """
    image = SimpleImage('images/Maddie.jpg')
    pixel_image = pixelate(image)  # call function that pixelates image
    #image.show()
    #pixel_image.show()


def pixelate(image):
    """
    Function that replaces pixel from target image with pixel from a set color palette
    and returns a copy of the image using on colors from a set palette of colors
    """
    image_copy = SimpleImage.blank(image.width, image.height)
    for new_pixel in image_copy:
        x = new_pixel.x
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)
        palette_color = color_picker(old_pixel)
    return image_copy


def color_picker(pixel):
    """
    Function that takes in pixel from image and returns the pixel color from a palette
    which is the closest color
    :param pixel: RGB value of pixel
    :return: closest RGB value from palette
    """
    palette = [[0, 0, 0],
               [0, 0, 170],
               [0, 170, 1],
               [170, 0, 0],
               [0, 170, 170],
               [253, 255, 82],
               [253, 86, 252],
               [255, 255, 255]]
    for colors in palette:
        distance_list = []
        red = pixel.red
        green = pixel.green
        blue = pixel.blue
        distance = (colors[0] - red) ^ 2 + (colors[1] - green) ^ 2 + (colors[2] - blue) ^ 2
        print(distance)
    # color_value = palette.get(pixel)
    # return color_value


if __name__ == '__main__':
    main()
