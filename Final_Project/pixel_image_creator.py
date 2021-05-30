"""
This program takes an image and returns an image where each pixel
of the new image is the average of a 2x2 grid of pixels from the
starting image.
"""

from simpleimage import SimpleImage
import math


def main():
    image_list = ['dog.png', 'landscape.jpg']
    palette_list = ['cyber9.png', 'endesga32.png']

    print("List of files: ")
    for images in image_list:
        print(image_list.index(images) + 1, images)

    filename = input("\nGive me a filename: ")
    while True:
        try:
            image = SimpleImage(f'Images/{filename}')
            break
        except FileNotFoundError:
            filename = input("Give me a filename again: ")

    image_copy = shrink(image)

    image.show()

    new_image = pixelate(image_copy)

    pixel_image = expand(new_image)

    pixel_image.show()


def shrink(image):
    image_copy = SimpleImage.blank(image.width // 4, image.height // 4)

    y = 0
    x = 0
    x_coord = 0
    y_coord = 0
    while y < image.height - 2:
        while x < image.width - 2:
            image_copy.set_pixel(x_coord, y_coord, get_grid_average(x, y, image))
            x_coord += 1
            x += 4
        x = 0
        x_coord = 0
        y_coord += 1
        y += 4
    return image_copy


def get_grid_average(x, y, image):
    """
    Function that takes in an x and y coordinate for a pixel on an image and
    returns the average of the colors of a range that is 2x2 starting at that coordinate.
    :param x: x coordinate in image
    :param y: y coordinate in image
    :param image: image to obtain colors from
    :return: average pixel color over 2x2 grid area
    """
    red = []
    green = []
    blue = []
    counter = 0
    for i in range(x, x + 4):
        for j in range(y, y + 4):
            pixel = image.get_pixel(i, j)
            red.append(pixel.red)
            green.append(pixel.green)
            blue.append(pixel.blue)
            counter += 1
    pixel.red = sum(red) // counter
    pixel.green = sum(green) // counter
    pixel.blue = sum(blue) // counter
    return pixel


def expand(image):
    expanded_image = SimpleImage.blank(image.width * 4, image.height * 4)

    y = 0
    x = 0
    x_coord = 0
    y_coord = 0
    while y < image.height:
        while x < image.width:
            expanded_image.set_pixel(x_coord, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 3, image.get_pixel(x, y))
            x_coord += 4
            x += 1
        x = 0
        x_coord = 0
        y_coord += 4
        y += 1

    return expanded_image


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
    :param palette: User palette choice
    :param pixel: RGB value of pixel
    :return: closest RGB value from palette
    """
    palette = SimpleImage('Palettes/endesga32.png')

    palette_list = []

    for color in palette:
        rgb_list = [color.red, color.green, color.blue]
        palette_list.append(rgb_list)

    distance_list = []

    for color in palette_list:
        distance = int(math.sqrt((pixel.red - color[0]) ** 2 + (pixel.green - color[1]) ** 2 +
                                 (pixel.blue - color[2]) ** 2))
        distance_list.append(distance)

    closest_color = min(distance_list)
    location = distance_list.index(closest_color)
    return palette_list[location]


if __name__ == '__main__':
    main()
