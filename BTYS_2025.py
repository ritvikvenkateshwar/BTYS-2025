#import the required libraries
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import seaborn as sea
import warnings
import pycoral
from tensorflow.lite.python.util import populate_conversion_metadata
import os
from PIL import Image, ImageDraw


#import the data

image = Image.open("C:\\Users\\vvenkata\\Desktop\\coding stuff\\BTYS_2025\\Eye Scans\\Independent Test Set\\Independent Test Set\\Keratoconus\\case1\\KCN_1_CT_A.jpg")
imgplot = plt.imshow(img)
#format the data

#train the model

#validate the model

#convert to TFlite
"""saved_keras_model = 'model.h5'
model.save(saved_keras_model)

converter = tf.lite.TFLiteConverter.from_keras_model_file(saved_keras_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

with open('mobilenet_v2_1.0_224.tflite', 'wb') as f:
  f.write(tflite_model)"""

#Convert to Tensor Processing Unit(hehe cute box)

