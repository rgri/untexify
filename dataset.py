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

# .Path()'s need an absolute path
data_dir = pathlib.Path("/home/shortcut/git/untexify/images")
image = cv2.imread("/home/shortcut/git/untexify/images/0/0.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

transform = A.Compose([A.ElasticTransform(alpha=2, sigma=0.9, alpha_affine=10, p=1)])
for i in range(53):
    imagePath = "/home/shortcut/git/untexify/original_images/" + str(i) + ".png"
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for j in range(200):
        # sigma is "squiggliness", alpha is movement?, alpha_affine is how much it moves across the page
        transformed = transform(image=image)["image"]
        transformed = np.array(transformed)
        outName = "/home/shortcut/git/untexify/images/" + str(i) + "/" + str(j) + ".png"
        cv2.imwrite(outName, transformed)
