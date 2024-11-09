import numpy as np
import matplotlib.pyplot as plt
import sys
import arr1d
import printing_tool as pt


def _1d(a, b):
  # Convert a and b to 1d arrays
  arr_a = arr1d.arr1d(a)
  arr_b = arr1d.arr1d(b)
  # Exchange the values of the arrays
  arr_a.swap(arr_b)
  # Convert the arrays to images
  ra = arr_a.to_img()
  rb = arr_b.to_img()
  return ra, rb


if __name__ == '__main__':
  a = sys.argv[1]
  b = sys.argv[2]
  # Load images
  im_a = plt.imread(a)
  im_b = plt.imread(b)
  # Convert rgb to grayscale
  im_a = np.dot(im_a[...,:3], [0.299, 0.587, 0.114])
  im_b = np.dot(im_b[...,:3], [0.299, 0.587, 0.114])
  # Apply transformation
  print("Processing...")
  res_a, res_b = _1d(im_a, im_b)
  # Print results
  pt.pt(im_a, im_b, res_a, "out/01-grayscale", False)
  pt.pt(im_b, im_a, res_b, "out/01-grayscale", False)
  print("Done.")
