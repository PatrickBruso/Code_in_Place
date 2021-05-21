"""
This program takes an image and returns an image where each pixel
of the new image is the average of a 4x4 grid of pixels from the
starting image.
"""

from simpleimage import SimpleImage


def main(image):
    image_copy = SimpleImage.blank(image.width, image.height)

    height_start = 0
    width_start = 0
    height_counter = 4
    width_counter = 4
    while height_counter < image.height:
        for x in range(height_start, height_counter):
            for y in range(width_start, width_counter):
                pixel = image.get_pixel(x, y)
                average_color = pixel_average(pixel)
        height_start += 4
        width_start += 4
        height_counter += 4
        width_counter += 4
        """
        I think I wanted nested loops that are in a separate function.  So we have a function that does the 
        range for x and y that's 4 each time for each, then takes the average of each pixel, then returns the average.
        Then I want another loop of some type (while or for) which calls that function.  So you would have a new range
        that is the height and width divided by 4 and then you call the function to grid for each range.
        for i in range(height // 4):
            call_function(grid_size)
        """


def pixel_average(pixel):
    # determine average of pixel to check against threshold
    return (pixel.red + pixel.blue + pixel.green) // 3


if __name__ == '__main__':
    main()