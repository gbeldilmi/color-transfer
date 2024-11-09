import numpy as np
import matplotlib.pyplot as plt
import sys
import arr3d
import printing_tool as pt


def _bij(a, b):
  # Convert a and b to 3d arrays
  arr_a = arr3d.arr3d(a)
  arr_b = arr3d.arr3d(b)
  # Create a bijection between the pixels of the two arrays
  arr_a.bijection(arr_b)
  # Convert the arrays to images
  res = arr_a.to_img()
  return res

if __name__ == '__main__':
  # Get the images paths
  a = sys.argv[1]
  b = sys.argv[2]
  # Load images
  im_a = plt.imread(a)
  im_b = plt.imread(b)
  im_a_norm = (im_a-np.min(im_a))/(np.max(im_a)-np.min(im_a)) * 255
  im_b_norm = (im_b-np.min(im_b))/(np.max(im_b)-np.min(im_b)) * 255
  # Crop the images to 100x100 (for memory reasons)
  im_a = im_a[:100, :100]
  im_b = im_b[:100, :100]
  im_a_norm = im_a_norm[:100, :100]
  im_b_norm = im_b_norm[:100, :100]
  # Apply the 3d transformation to the images
  print("Processing...")
  print("0/2", end="\r")
  res_a = _bij(im_a_norm, im_b_norm)
  pt.pt(im_a, im_b, res_a, "out/04-bijection", False)
  print("1/2", end="\r")
  res_b = _bij(im_b_norm, im_a_norm)
  pt.pt(im_b, im_a, res_b, "out/04-bijection", False)
  print("2/2", end="\r")
  # Print results
  print("Done.")

