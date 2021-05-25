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
    palette = [[13, 43, 69],
               [32, 60, 86],
               [84, 78, 104],
               [141, 105, 122],
               [208, 129, 89],
               [255, 170, 94],
               [255, 212, 163],
               [255, 236, 214]]

    for i in range(len(palette)):
        for value in palette[i]:
            print(value[0])
            print(value[1])
            print(value[2])
            distance_list = []
            distance = math.sqrt((palette[i][j] - pixel.red) ** 2 + (color[1] - pixel.green) ** 2 + (color[2] - pixel.blue) ** 2)
            # create pixels and put those into a list?
            for x in range(8):
                for y in range(8):
                    pixel_list = [image.get_pixel(x, y)]

        # strip list items into separate integers?
        x = 0  # counter maybe don't need
        # compare palette[i] to pixel and then put distances into list.
        # take list and find the smallest value.
        # get the location in list of smallest value and match to palette list.
        # return that value of palette list (for example palette[location of smallest in list]
        #print(palette[i])

    """
    for color in palette:
        distance_list = []
        distance = math.sqrt((color[0] - pixel.red) ** 2 + (color[1] - pixel.green) ** 2 + (color[2] - pixel.blue) ** 2)
        distance_list.append(distance)
        print(distance_list)
    # color_value = palette.get(pixel)
    # return color_value
    """


if __name__ == '__main__':
    main()
