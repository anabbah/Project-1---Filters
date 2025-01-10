'''
Amarachi Abbah
10NOV24
COMP 163/006
My mission in this challenge is to put a green border with
a pixel size of 10 around the dog in the image.
'''
from PIL import Image
from image_converter import ListToImage, ImageToList

def add_border(pixels):
  """ add_border creates a green border around the dog. """
  new_border = []
  num_rows = len(pixels)
  for row_index,row in enumerate(pixels):
    colored_row = []
    num_columns = len(row)
    for col_index,col in enumerate(row):
      if row_index < 10:
        colored_row.append((0,255,0))
      elif row_index >= num_rows-10:
        colored_row.append((0,255,0))
      elif col_index < 10:
        colored_row.append((0,255,0))
      elif col_index >= num_columns-10:
        colored_row.append((0,255,0))
      else:
        colored_row.append(col)
      #if row_index == 0:
        #pixels[0] = (0,255,0)
    new_border.append(colored_row)
      #else:

  return new_border
  # Convert to have a green border.
  #pass


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = add_border(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/border.png")
