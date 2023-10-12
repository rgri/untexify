import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib

from tensorflow import keras
from keras import layers
from keras.models import Sequential

model = keras.models.load_model("/home/shortcut/git/untexify/frontend/untexifyweb/testapp/static/testapp/webmodel/")
class_names = [
    "cap",
    "cup",
    "geq",
    "geqslant",
    "gg",
    "ggg",
    "greaterthan",
    "in",
    "leq",
    "leqslant",
    "lessthan",
    "ll",
    "lll",
    "mathbb{A}",
    "mathbb{C}",
    "mathbb{H}",
    "mathbb{N}",
    "mathbb{O}",
    "mathbb{Q}",
    "mathbb{R}",
    "mathbb{S}",
    "mathbb{Z}",
    "ngeq",
    "ngeqslant",
    "ngtr",
    "ni",
    "nleq",
    "nleqslant",
    "nless",
    "not ubset",
    "not upset",
    "notin",
    "nprec",
    "npreceq",
    "nsubseteq",
    "nsucc",
    "nsucceq",
    "nsupseteq",
    "prec",
    "preceq",
    "setminus",
    "sqsubset",
    "sqsupset",
    "subset",
    "subset2",
    "subseteq",
    "subseteq2",
    "succ",
    "succeq",
    "supset",
    "supset2",
    "supseteq",
    "supseteq2",
]


image = tf.keras.utils.load_img("myinput.png", color_mode="grayscale")
image_array = tf.keras.utils.img_to_array(image)
img_array = tf.expand_dims(image_array, 0)
class_names[np.argmax(tf.nn.softmax(model(img_array)))]
