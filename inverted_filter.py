'''
Amarachi Abbah
10NOV24
COMP 163/006
My mission in this challenge is to make my own filter
for the dog.
'''
from PIL import Image
from image_converter import ListToImage, ImageToList

def yours(pixels):
  """ my program makes the bright pixels bright on 
  the dog and turns the rest of the pixels dark. """
  modified_list = []
  for row in pixels:
    modified_row = []
    modified_list.append(modified_row)
    for pixel in row:
      R,G,B = pixel
      rgb_avg = (R+G+B)//3
      if rgb_avg <= 150:
        new_pixels = (rgb_avg,rgb_avg,rgb_avg)
      elif rgb_avg == 120:
        new_pixels = (rgb_avg,rgb_avg,rgb_avg)
      else:
        new_pixels = (R,G,B)
      modified_row.append(new_pixels)

  return modified_list

  # Convert to have a green border.


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = yours(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/yours.png")
