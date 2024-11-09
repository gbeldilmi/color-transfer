import numpy as np
import matplotlib.pyplot as plt
import sys
import arr3d
import printing_tool as pt


def _3d(a, b, fn, arg):
  # Convert a and b to 3d arrays
  arr_a = arr3d.arr3d(a)
  arr_b = arr3d.arr3d(b)
  # Transfer
  if fn == 'dist':
    arr_a.transfer_by_distance(arr_b, arg)
  elif fn == 'iter':
    arr_a.transfer_by_iteration(arr_b, arg)
  elif fn == 'list':
    arr_a.transfer_by_vector_list(arr_b, arg)
  # Convert the arrays to images
  ra = arr_a.to_img()
  return ra 


if __name__ == '__main__':
  ##################################################################################################
  # Parameters (change these values to adjust the behavior of the program)                         #
  ##################################################################################################
  NB_ITER = 20      # Number of iterations
  EPSILON = 5       # Acceptable distance between the two images
  VEC_LIST = [      # List of vectors to use
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1)
  ]
  ##################################################################################################
  # Get the images paths
  a = sys.argv[1]
  b = sys.argv[2]
  # Load images
  im_a = plt.imread(a)
  im_b = plt.imread(b)
  im_a_norm = (im_a-np.min(im_a))/(np.max(im_a)-np.min(im_a)) * 255
  im_b_norm = (im_b-np.min(im_b))/(np.max(im_b)-np.min(im_b)) * 255
  # Apply the 3d transformation to the images
  print("Processing...")
  print("0/6", end="\r")
  res_a = _3d(im_a_norm, im_b_norm, 'dist', EPSILON)
  print("1/6", end="\r")
  res_b = _3d(im_a_norm, im_b_norm, 'iter', NB_ITER)
  print("2/6", end="\r")
  res_c = _3d(im_a_norm, im_b_norm, 'list', VEC_LIST)
  print("3/6", end="\r")
  res_d = _3d(im_b_norm, im_a_norm, 'dist', EPSILON)
  print("4/6", end="\r")
  res_e = _3d(im_b_norm, im_a_norm, 'iter', NB_ITER)
  print("5/6", end="\r")
  res_f = _3d(im_b_norm, im_a_norm, 'list', VEC_LIST)
  print("6/6", end="\r")
  # Print results
  pt.pt(im_a, im_b, res_a, "out/03-transfer-dist", False)
  pt.pt(im_a, im_b, res_b, "out/03-transfer-iter", False)
  pt.pt(im_a, im_b, res_c, "out/03-transfer-list", False)
  pt.pt(im_b, im_a, res_d, "out/03-transfer-dist", False)
  pt.pt(im_b, im_a, res_e, "out/03-transfer-iter", False)
  pt.pt(im_b, im_a, res_f, "out/03-transfer-list", False)
  print("Done.")
