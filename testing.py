import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib
import albumentations as A
import cv2
import scipy

from tensorflow import keras
from keras import layers
from keras.models import Sequential

modelPath = "model.tflite"

interpreter = tf.lite.Interpreter(model_path=modelPath)

classify_lite = interpreter.get_signature_runner("serving_default")

image = tf.keras.utils.load_img("myinput.png")
image_array = tf.keras.utils.img_to_array(image)
img_array = tf.expand_dims(image_array, 0)

prediction = classify_lite(rescaling_1_input=img_array)
array = np.array(prediction)
guess = np.argmax(tf.nn.softmax(prediction["dense_3"]))
print(guess)
