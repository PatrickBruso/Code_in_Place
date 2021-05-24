"""
This program takes an image and returns an image where each pixel
of the new image is the average of a 2x2 grid of pixels from the
starting image.
"""

from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/landscape.jpg')
    image_copy = SimpleImage.blank(image.width, image.height)

    y = 0
    x = 0
    new_x = 0
    new_y = 0
    red = 0
    green = 0
    blue = 0
    num = 0
    while y < image.height:
        while x < image.width:
            for i in range(x, x + 2):
                for j in range(y, y + 2):
                    pixel = image.get_pixel(i, j)
                    red += pixel.red
                    green += pixel.green
                    blue += pixel.blue
                    num += 1
            pixel.red = red
            pixel.green = green
            pixel.blue = blue
            image_copy.set_pixel(new_x, new_y, pixel_average(pixel, num))
            new_x += 1
        x += 2
        new_y += 1
    y += 2

    # image_copy.show()


def get_grid_average(x, y, image):
    red = []
    green = []
    blue = []
    for i in range(x, x+2):
        for j in range(y, y+2):
            pixel = image.get_pixel(i, j)
            red.append(pixel.red)
            green.append(pixel.green)
            blue.append(pixel.blue)


def pixel_average(pixel, num):
    # determine average of pixel to check against threshold
    return (pixel.red + pixel.blue + pixel.green) // num


if __name__ == '__main__':
    main()
