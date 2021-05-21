"""
Program that takes in an image and shows a pixelated copy
1. Get image to pixelate
2. Determine what size grids to use (9x9, 4x4, etc)
3. Create new image of the appropriate size
4. For each grid, determine average color
5. For each grid color, write color to pixel on new image
6. Return image and new image
"""

from simpleimage import SimpleImage


def main():
    filename = input("Give me a filename ")
    while True:
        try:
            image = SimpleImage(f'images/{filename}')
            break
        except FileNotFoundError:
            filename = input("Give me a filename again ")

    grid_size = grid(image)  # call function to determine grid size to use
    pixel_image = pixelate(image, grid_size)  # call function that pixelates image
    downscale_image = downscale(image)
    image.show()
    downscale_image.show()


def grid(image):
    # need to work on this function to determine if the grid sizes will fit the image dimensions
    # if image.width and image.height % 9 == 0:
    return 9


def pixelate(image, size):
    image_copy = SimpleImage.blank(image.width // size, image.height // size)
    """
    use some get function that takes the pixel location and 
    returns the first grid? so for pixel 0,0 returns 0-9, 0-9?
    
    what if you had a counter that was set to width // 9 and another for height // 9 and then each
    iteration you decreased the counter in a while loop so that when it hit zero you would know that 
    the grid sections were done?
    """
    for new_pixel in image_copy:
        x = new_pixel.x  # turn x and y into ranges?
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)  # or use get_pixel to get a range of pixels? nested loop?

        """
        for i in range(image.height // 9):
            for j in range(9)
        """
        # write the color using the average function
    return image_copy


def average(image, size):
    return 10
    # function that takes grid area of original image and returns the average color for that grid


def downscale(image):
    """
    Function that takes an image and for each pixel returns a new pixel that contains one of eight
    primary colors.
    :param image: original image
    :return: copy of image pixelated
    """
    downscaled_copy = SimpleImage.blank(image.width, image.height)
    for new_pixel in downscaled_copy:
        x = new_pixel.x
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)

        color_red = str((old_pixel.red // 128))
        color_green = str((old_pixel.green // 128))
        color_blue = str((old_pixel.blue // 128))
        color_key = color_red + color_blue + color_green

        color = color_picker(color_key)

        new_pixel.red = color[0]
        new_pixel.green = color[1]
        new_pixel.blue = color[2]

        downscaled_copy.set_pixel(x, y, new_pixel)
    return downscaled_copy


def color_picker(pixel):
    """
    Function that takes in a string of 3-bit rgb values and compares to a dict returning
    the rgb value to be used for that pixel using a palette of 8 colors.
    :param pixel: string of 3-bit values
    :return: pixel with rgb values
    """
    colors = {'000': [0, 0, 0],
              '001': [0, 0, 255],
              '010': [0, 255, 0],
              '100': [255, 0, 0],
              '011': [0, 255, 255],
              '110': [255, 255, 0],
              '101': [255, 0, 255],
              '111': [255, 255, 255]}
    color_value = colors.get(pixel)
    return color_value


if __name__ == '__main__':
    main()
