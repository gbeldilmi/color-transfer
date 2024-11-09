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
  # Extract each channel from images
  im_a_r = im_a[...,0]
  im_a_g = im_a[...,1]
  im_a_b = im_a[...,2]
  im_b_r = im_b[...,0]
  im_b_g = im_b[...,1]
  im_b_b = im_b[...,2]
  # Apply transformation to each channel
  print("Processing...")
  res_a_r, res_b_r = _1d(im_a_r, im_b_r)
  res_a_g, res_b_g = _1d(im_a_g, im_b_g)
  res_a_b, res_b_b = _1d(im_a_b, im_b_b)
  # Recombine channels
  w, h, c = im_a.shape
  res_a = np.zeros((w, h, c))
  res_b = np.zeros((w, h, c))
  res_a[:, :, 0] = res_a_r
  res_a[:, :, 1] = res_a_g
  res_a[:, :, 2] = res_a_b
  res_b[:, :, 0] = res_b_r
  res_b[:, :, 1] = res_b_g
  res_b[:, :, 2] = res_b_b
  ma = np.max(res_a)
  mb = np.max(res_b)
  res_a /= ma
  res_b /= mb
  # Print results
  pt.pt(im_a, im_b, res_a, "out/02-colors", False)
  pt.pt(im_b, im_a, res_b, "out/02-colors", False)
  print("Done.")
