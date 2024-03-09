import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import gass
def show_img(title, image):
  cv.imshow(title, image)
  cv.waitKey(0)
  cv.destroyAllWindows()
import cv2
import os
def get_data(path):
  pixels = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  new_size = (128, 128)
  pixels = cv2.resize(pixels, new_size)
  edges=gass.edgedetectusingcannyandgaussian(pixels)
  processed_image = cv.normalize(edges, None, alpha = 0, beta = 1,
  norm_type=cv.NORM_MINMAX, dtype = cv.CV_32F)
# processed_image = np.expand_dims(processed_image, axis=2)
  processed_image = np.reshape(processed_image, (128, 128, 1))
#print(processed_image)
# show_img("Normalized Image", processed_image)
# raw_images.append(pixels)
# processed_images.append(processed_image)
  label=None
  if str(path[-6:])=="KS.png":
   label = 1
  elif str(path[-5:])=="N.png":
   label = 0
  return pixels, processed_image, label
def find_edge_and_normalize():
  raw_images = []
  processed_images = []
  labels = []
  src_folder="KidneyStones"
  for file in os.listdir(src_folder):
    pixels = cv2.imread(src_folder + "/" + file, cv2.IMREAD_GRAYSCALE)
    new_size = (128, 128)
    pixels = cv2.resize(pixels, new_size)
    edges=gass.edgedetectusingcannyandgaussian(pixels)
    processed_image = cv.normalize(edges, None, alpha = 0, beta = 1,
    norm_type=cv.NORM_MINMAX, dtype = cv.CV_32F)
# processed_image = np.expand_dims(processed_image, axis=2)
    processed_image = np.reshape(processed_image, (128, 128, 1))
#print(processed_image)
# show_img("Normalized Image", processed_image)
    raw_images.append(pixels)
    processed_images.append(processed_image)
    if str(file[-6:])=="KS.png":
      labels.append(1)
    elif str(file[-5:])=="N.png":
      labels.append(0)
  return np.array(raw_images), np.array(processed_images), np.array(labels)
import cnn
def maincode(path):
# if name ==" main ":
  LIMIT = -5
  raw_images, processed_images, labels = find_edge_and_normalize()
  model = keras.models.load_model("saved_model")
  image_path = path;
  raw_image, processed_image, label = get_data(image_path)
  f, axarr = plt.subplots(1, 3)
  processed = processed_image.reshape(128, 128)
  axarr[0].imshow(raw_image)
  axarr[1].imshow(processed, cmap='gray')
  prediction = model.predict(np.array([processed_image]))
  processed = processed_image.reshape(128, 128)
  if prediction[0] >= 0.75:
   result = 'yes'
  else:
   result = 'no'
  output = raw_image.copy()
  output_img = cv.putText(output, result, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2, cv2.LINE_AA)
  axarr[2].imshow(output_img)
  plt.savefig("output")