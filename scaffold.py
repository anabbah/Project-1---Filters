'''
Amarachi Abbah
10NOV24
COMP 163/006
My mission in this challenge is to convert
the pixels of R G B values and turn it into grayscale.
'''
from PIL import Image
from image_converter import ListToImage, ImageToList


def grayscale(pixels):
  """ grayscale converts the RGB in pixels to grayscale. """
  # Covert to grayscale.
  
  grayscale_list = []
  for row in pixels:
    grayscale_row = []
    grayscale_list.append(grayscale_row)
    for pixel in row:
      R,G,B = pixel
      rgb_avg = (R+G+B)//3
      new_pixels = (rgb_avg,rgb_avg,rgb_avg)
      grayscale_row.append(new_pixels)
  return grayscale_list


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)
  #print(pixels)

  # Apply the filter.
  filtered_pixels = grayscale(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/grayscale.png")
