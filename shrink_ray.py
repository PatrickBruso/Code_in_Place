"""
This program takes an image and returns an image where each pixel
of the new image is the average of a 2x2 grid of pixels from the
starting image.
"""

from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/landscape.jpg')
    image_copy = SimpleImage.blank(image.width, image.height)
    get_grid_average(0, 0, image)
    """
    y = 0
    x = 0
    x_coord = 0
    y_coord = 0
    while y < image.height:
        while x < image.width:
            get_grid_average(x_coord, y_coord, image) # combine with next line?
            image_copy.set_pixel(new_x, new_y, pixel_average(pixel, num))
            x_coord += 1
        x += 2
        y_coord += 1
    y += 2

    # image_copy.show()
    """


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
    for i in range(x, x+2):
        for j in range(y, y+2):
            pixel = image.get_pixel(i, j)
            red.append(pixel.red)
            green.append(pixel.green)
            blue.append(pixel.blue)
            counter += 1
    pixel.red = sum(red) // counter
    pixel.green = sum(green) // counter
    pixel.blue = sum(blue) // counter
    return pixel


def pixel_average(pixel, num):
    # determine average of pixel to check against threshold
    return (pixel.red + pixel.blue + pixel.green) // num


if __name__ == '__main__':
    main()
