import numpy as np
import random as rd


class p1d:
  # This class represents a pixel of the image with its value and its coordinates
  # It is used to store the pixels of the image in a 1d array and still be able to restore the image
  def __init__(self, val, x, y):
    self.val = val
    self.x, self.y = x, y


class arr1d:
  def __init__(self, img):
    # Get the shape of the image
    self.h, self.w = img.shape
    # Create an array of p1d objects with the pixels of the image
    self.arr = []
    for i in range(self.h):
      for j in range(self.w):
        self.arr.append(p1d(img[i, j], i, j)) # Value, X, Y

  def swap(self, b):
    # Use a bijection to exchange the values of the arrays but keep the coordinates
    # Both arrays must have the same length, same type and be sorted
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr1d), "Both arrays must be of the same type"
    self.arr = sorted(self.arr, key=lambda x: x.val)
    b.arr = sorted(b.arr, key=lambda p: p.val)
    # The value of the n-th element of a will be the value of the n-th element of b and vice versa
    for i in range(len(self.arr)):
      self.arr[i].val, b.arr[i].val = b.arr[i].val, self.arr[i].val

  def to_img(self):
    # Create an image with the same shape as the original image
    res = np.zeros((self.h, self.w))
    # Fill the image with the values of the array
    for i in self.arr:
      res[i.x, i.y] = i.val
    return res
