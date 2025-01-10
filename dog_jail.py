'''
Amarachi Abbah
10NOV24
COMP 163/006
My mission in this challenge is to put the dog in jail.
'''

from PIL import Image
from image_converter import ListToImage, ImageToList

def jail(pixels):
  """ jail changes the rgb of the pixels and puts a
  purple jail over every 10th column using mod """
  # Convert to jail.
  grayscale_list = []
  for row in pixels:
    grayscale_row = []
    grayscale_list.append(grayscale_row)
    for row_index,row in enumerate(row):
      if row_index % 10 == 0:
        pixels = (128,0,128)
      else:
        pixels = row
      grayscale_row.append(pixels)
  return grayscale_list


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = jail(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/jail.png")
