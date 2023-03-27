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
data_dir = pathlib.Path("/home/shortcut/git/untexify-data/images")

# TODO: Explain the reasoning for this choice of transforms.
transform = A.Compose(
    [
        A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        A.ElasticTransform(alpha=20, sigma=10000, alpha_affine=10, p=1),
        A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        A.Equalize(p=1.0),
    ]
)

# Displays before and after images of the transform stack being applied to a sample image.
#
# image = cv2.imread("/home/shortcut/git/untexify-data/original_images/0.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(image)
# plt.show()
# transformed = transform(image=image)["image"]
# plt.imshow(transformed)
# plt.show()

# Generate the dataset
for i in range(53):
    print(i)
    print()
    imagePath = "/home/shortcut/git/untexify-data/original_images/" + str(i) + ".png"
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for j in range(200):
        if j % 50 == 0:
            print(j)
            print()
        # sigma is "squiggliness", alpha is movement?, alpha_affine is how much it moves across the page
        # TODO: Clean up this comment.
        transformed = transform(image=image)["image"]
        transformed = np.array(transformed)
        outName = (
            "/home/shortcut/git/untexify-data/images/" + str(i) + "/" + str(j) + ".png"
        )
        cv2.imwrite(outName, transformed)
