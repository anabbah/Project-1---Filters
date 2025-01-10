'''
Amarachi Abbah
10NOV24
COMP 163/006
My mission in this challenge is to implement a norak filter
on the dog
'''
from PIL import Image
from image_converter import ListToImage, ImageToList
      
 
def norak(pixels):
  """ norak takes the pixels that have an avg over 153
  and sets it to its average component. these are
  bright pixels. """

  grayscale_list = []
  for row in pixels:
    grayscale_row = []
    grayscale_list.append(grayscale_row)
    for pixel in row:
      R,G,B = pixel
      rgb_avg = (R+G+B)//3
      if rgb_avg > 153:
        new_pixels = (rgb_avg,rgb_avg,rgb_avg)
      else:
        new_pixels = (R,G,B)
      grayscale_row.append(new_pixels)

  return grayscale_list

  # Convert to norak.


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = norak(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/norak.png")
