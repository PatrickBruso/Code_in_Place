from simpleimage import SimpleImage


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
