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
    image.show()
    pixel_image.show()


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
        new_pixel.red = palette_color[0]
        new_pixel.green = palette_color[1]
        new_pixel.blue = palette_color[2]
        image_copy.set_pixel(x, y, new_pixel)
    return image_copy


def color_picker(pixel):
    """
    Function that takes in pixel from image and returns the pixel color from a palette
    which is the closest color
    :param pixel: RGB value of pixel
    :return: closest RGB value from palette
    """
    palette = [[13, 43, 69],
               [32, 60, 86],
               [84, 78, 104],
               [141, 105, 122],
               [208, 129, 89],
               [255, 170, 94],
               [255, 212, 163],
               [255, 236, 214]]

    palette_2 = [[190, 74, 47],
                 [215, 118, 67],
                 [234, 212, 170],
                 [228, 166, 114],
                 [184, 111, 80],
                 [115, 62, 57],
                 [62, 39, 49],
                 [162, 38, 51],
                 [228, 59, 68],
                 [247, 118, 34],
                 [254, 174, 52],
                 [254, 231, 97],
                 [99, 199, 77],
                 [62, 137, 72],
                 [38, 92, 66],
                 [25, 60, 62],
                 [18, 78, 137],
                 [0, 153, 219],
                 [44, 232, 245],
                 [255, 255, 255],
                 [192, 203, 220],
                 [139, 155, 180],
                 [90, 105, 136],
                 [58, 68, 102],
                 [38, 43, 68],
                 [24, 20, 37],
                 [255, 0, 68],
                 [104, 56, 108],
                 [181, 80, 136],
                 [246, 117, 122],
                 [232, 183, 150],
                 [194, 133, 105]]

    distance_list = []

    for color in palette_2:
        distance = int(math.sqrt((color[0] - pixel.red) ** 2 + (color[1] - pixel.green) ** 2 +
                                 (color[2] - pixel.blue) ** 2))
        distance_list.append(distance)

    closest_color = min(distance_list)
    location = distance_list.index(closest_color)
    return palette_2[location]


if __name__ == '__main__':
    main()
