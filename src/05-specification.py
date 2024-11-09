import numpy as np
import matplotlib.pyplot as plt
import sys
import arr3d
import printing_tool as pt


def _sp(a, b, order):
  # Convert a and b to 3d arrays
  arr_a = arr3d.arr3d(a)
  arr_b = arr3d.arr3d(b)
  # Use the specification method between the pixels of the two arrays
  arr_a.specification(arr_b, order)
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
  # Apply the 3d transformation to the images and print the results
  orders = ["rgb", "rbg", "grb", "gbr", "brg", "bgr"]
  print("Processing...")
  print("0/12", end="\r")
  for i in range(12):
    if i < 6:
      res = _sp(im_a_norm, im_b_norm, orders[i])
      pt.pt(im_a, im_b, res, f"out/05-specification-{orders[i]}", False)
    else:
      res = _sp(im_b_norm, im_a_norm, orders[i-6])
      pt.pt(im_b, im_a, res, f"out/05-specification-{orders[i-6]}", False)
    print(f"{i+1}/12", end="\r")
  print("Done.")

