import numpy as np
import random as rd
import math


class p3d:
  # This class represents a pixel of the image with its rgb values and its coordinates
  # It is used to store the pixels of the image in a 1d array and still be able to restore the image
  def __init__(self, r, g, b, x, y):
    self.r, self.g, self.b = r, g, b
    self.x, self.y = x, y


class arr3d:
  def __init__(self, img):
    # Get the shape of the image
    self.h, self.w, _ = img.shape
    # Get the center of the cloud of points in the rgb space
    self.max = np.max(img)
    if self.max <= 1:
      self.max = 1
    else:
      self.max = 255
    # Create an array of p3d objects with the pixels of the image
    self.arr = []
    for i in range(self.h):
      for j in range(self.w):
        self.arr.append(p3d(*img[i, j], i, j)) # R, G, B, X, Y

  def bijection(self, b):
    # Create a bijection between the pixels of the two arrays
    # by choosing the closest pixels in each rgb space
    def distance(p1, p2): # Get the distance between two pixels in the rgb space
      return math.sqrt((p1.r - p2.r) ** 2 + (p1.g - p2.g) ** 2 + (p1.b - p2.b) ** 2)
    def get_adjacency_matrix(a, b): # Get the adjacency matrix of the pixels of the two arrays
      m = np.full((len(a), len(b)), np.inf)
      for i in range(len(a)):
        for j in range(len(b)):
          m[i][j] = distance(a[i], b[j])
      return m
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    # Get the adjacency matrix of the pixels of the two arrays
    adj = get_adjacency_matrix(self.arr, b.arr)
    for u in range(len(self.arr)):
      # Get the indices of the minimum value of the adjacency matrix
      i, j = np.unravel_index(adj.argmin(), adj.shape)
      # Swap the RGB values of the pixels in the two arrays
      self.arr[i].r = b.arr[j].r
      self.arr[i].g = b.arr[j].g
      self.arr[i].b = b.arr[j].b
      # Replace the row and column of the minimum value by infinity
      adj[i, :] = np.inf
      adj[:, j] = np.inf

  def specification(self, b, order="rgb"):
    # First interpretation of the histogram specification method applied to 3d arrays
    def get_key_function(order):
      if order == "rgb":
        return lambda x: (x.r, x.g, x.b)
      elif order == "rbg":
        return lambda x: (x.r, x.b, x.g)
      elif order == "grb":
        return lambda x: (x.g, x.r, x.b)
      elif order == "gbr":
        return lambda x: (x.g, x.b, x.r)
      elif order == "brg":
        return lambda x: (x.b, x.r, x.g)
      elif order == "bgr":
        return lambda x: (x.b, x.g, x.r)
      else:
        return None
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    # Get the lambda function used to sort the pixels
    k = get_key_function(order)
    assert k is not None, "Invalid specified order"
    # Sort the pixels to combine the closest pixels
    self.arr = sorted(self.arr, key=k)
    b.arr = sorted(b.arr, key=k)
    # Replace RGB values of pixels in self.arr by the RGB values of the pixels in b.arr
    for i in range(len(self.arr)):
      self.arr[i].r = b.arr[i].r
      self.arr[i].g = b.arr[i].g
      self.arr[i].b = b.arr[i].b

  def to_img(self):
    # Create an image with the same shape as the original image
    res = np.zeros((self.h, self.w, 3))
    # Fill the image with the values of the array
    for i in self.arr:
      res[i.x, i.y, 0] = int(i.r)
      res[i.x, i.y, 1] = int(i.g)
      res[i.x, i.y, 2] = int(i.b)
    # Normalize the values of the array to the range [0, max]
    res = (res - np.min(res)) / (np.max(res) - np.min(res)) * self.max
    res = np.uint8(res)
    return res

  def transfer(self, b, vector=None):
    # Use sliced sliced optimal transport to move the values of the array to the values
    # of the array b in the rgb space
    def ratio(p): # Get the ratio between distance of the center and the projection and the vector
      return p.r * vector[0] + p.g * vector[1] + p.b * vector[2]
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    # If vector is undefined, generate a random vector
    if vector is None:
      r = rd.random() * 2 * np.pi
      s = rd.random() * np.pi
      vector = [np.sin(s) * np.cos(r), np.sin(s) * np.sin(r), np.cos(s)]
    # Project each pixel in the rgb space to the vector and sort the projections
    proj_a = sorted([(ratio(p), p) for p in self.arr], key=lambda x: x[0])
    proj_b = sorted([(ratio(p), p) for p in b.arr], key=lambda x: x[0])
    # Get the difference of the projections
    diff_proj = [proj_b[i][0] - proj_a[i][0] for i in range(len(proj_a))]
    # Get the average of the projections
    avg_diff_proj = sum(diff_proj) / len(diff_proj)
    # Move each pixel rgb value by the value of the difference of the projections
    for i in range(len(proj_a)):
      proj_a[i][1].r += diff_proj[i] * vector[0]
      proj_a[i][1].g += diff_proj[i] * vector[1]
      proj_a[i][1].b += diff_proj[i] * vector[2]
    # Return the average of the projections
    return avg_diff_proj

  def transfer_by_iteration(self, b, nb_iter):
    # Use the transfer method nb_iter times using random vectors
    for _ in range(nb_iter):
      self.transfer(b)

  def transfer_by_distance(self, b, epsilon):
    # Use the transfer method until the distance is less than epsilon
    last_distance = epsilon + 1
    while last_distance > epsilon:
      last_distance = self.transfer(b)

  def transfer_by_vector_list(self, b, vectors):
    # Use the transfer method with the given vectors
    for vector in vectors:
      self.transfer(b, vector)
