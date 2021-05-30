"""
This program takes an image and returns an image where each pixel
of the new image is the average of a 2x2 grid of pixels from the
starting image.
"""

from simpleimage import SimpleImage
from Final_Project.pixelator import pixelate
from Final_Project.expander import expand


def main():
    image_list = ['dog.png', 'landscape.jpg']

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


if __name__ == '__main__':
    main()
