"""
Program that takes in an image and assigns a color from a palette to each pixel
and returns a copy of the new image
"""

from simpleimage import SimpleImage
import math


def main():
    image_list = ['dog.png', 'landscape.jpg', 'Maddie.jpg', 'Seattle.jpg']
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

    pixel_image = pixelate(image)  # call function that pixelates image
    image.show()
    pixel_image.show()


def pixelate(image):
    """
    Function that replaces pixel from target image with pixel from a set color palette
    and returns a copy of the image using on colors from a set palette of colors
    """
    image_copy = SimpleImage.blank(image.width, image.height)
    """
    print("Palette options: \n1. Cybear - 9 colors \n2. Endesga - 32 colors \n3. Zughy - 32 colors")
    palette_choice = input("Enter choice: ")
    if palette_choice == 1:
        palette = 'cybear9.png'
    elif palette_choice == 2:
        palette = 'endesga32.png'
    else:
        palette = 'zughy32.png'
    """

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
    palette = SimpleImage('Palettes/cybear9.png')

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
