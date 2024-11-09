import datetime as dt
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np
import threading as th
import os


class pt: # Printing tool
  def __init__(self, img_a, img_b, img_result, title="plot", show=True, path=None):
    self.img_a = img_a
    self.img_b = img_b
    self.img_r = img_result
    self.title = title
    plt.rcParams["font.size"]=5
    self.__fig = plt.figure(title, figsize=(30, 30))
    self.__rows = 3
    self.__cols = 4 if img_a.shape[-1] == 3 else 2
    # self.__cols = 5 if img_a.shape[-1] == 3 else 2 # TO-DO : Uncomment this line when 3D representation is complete
    self.__nbplot = 0
    if not show:
      self.__printing_thread = th.Thread(target=self.__print)
      self.__printing_thread.start()
      self.__save(path)
    else:
      self.__print()

  def __print(self): # Prepare printing
    for it in [[self.img_a, "Image A"], [self.img_b, "Image B"], [self.img_r, "Result image"]]:
      if len(it[0].shape) == 2: # Grayscale
        self.__print_image(it[0], it[1])
        self.__print_histogram(it[0], it[1] + " histogram")
      else: # RGB
        self.__print_image(it[0], it[1]) # Images
        for i in range(3):
          self.__print_histogram(it[0][...,i], it[1] + " histogram (" + "RGB"[i] + ")") # Histograms
        #self.__print_3d(it[0], it[1]) # 3D representations # TO-DO : Uncomplete

  def __print_3d(self, img, title): # 3D representation # TO-DO : Uncomplete
    self.__nbplot += 1
    ax = self.__fig.add_subplot(self.__rows, self.__cols, self.__nbplot, projection='3d')
    # TO-DO : Uncomplete
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.set_title(title)

  def __print_histogram(self, channel_matrix, title): # Histogram
    self.__nbplot += 1
    ax = self.__fig.add_subplot(self.__rows, self.__cols, self.__nbplot)
    ax.hist(channel_matrix)
    ax.set_title(title)

  def __print_image(self, img, title): # Image
    self.__nbplot += 1
    ax = self.__fig.add_subplot(self.__rows, self.__cols, self.__nbplot)
    if img.shape[-1] == 3:
      ax.imshow(img)
    else:
      ax.imshow(img, cmap='gray')
    ax.set_title(title)

  def __show(self): # Show plot
    self.__print()
    self.__fig.show()

  def __save(self, path): # Save plot
    if path is None:
      current_time = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
      path = self.title.replace(" ", "_") + "_" + current_time + ".png"
    self.__printing_thread.join()
    # Create a the directory if it does not exist
    directory = "/".join(path.split("/")[:-1])
    if directory != "" and not os.path.exists(directory):
      os.makedirs(directory)
    self.__fig.savefig(path, dpi=300)


if __name__ == '__main__':
  a = np.random.rand(10, 10, 3)
  pt_show(a, a, a)
