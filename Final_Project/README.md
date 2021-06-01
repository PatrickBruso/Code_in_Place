# Code in Place 2021 - Final Project

<p>I have always been a fan of pixel art.  I'm not very good at creating it, however.  Since
a lot of this class focused on image manipulation using SimpleImage, I decided that I wanted 
to try and create a program that would pixelate a target image.  I thought this would be
possible since you can work with and manipulate pixels in SimpleImage.  
</p>

<p>My program has three parts.  First, it takes the target image and shrinks it by 4 times.
For each 4x4 grid of pixels (16 pixels) in the target image, one pixel is created in a copy
image that is the average of those 16 pixels.  Second, the program takes each pixel in the 
copied shrunken image,  and compares it to a palette of colors.  It uses the equation:
</p>

![Equation](Equation.png)

<p>to calculate the distance between two RGB colors.  The program will calculate the distance
for the target color and each color in a palette of colors to determine which is the closest.
It will then return that RGB value for the pixel.  Third, the program will then enlarge the
new pixelated image by 4x.  I found that shrinking and then enlarging the image helps to 
produce the "blocky" style that is commonly found in pixel art</p>

### Here is an example of the program:

target image:<br>
![Image of Landscape](Images/landscape.jpg)

Pixelated image:<br>
![Pixelated landscape](Pixel%20Images/pixelimage.png)