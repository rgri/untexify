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
from multiprocessing import Pool

from tensorflow import keras
from keras import layers
from keras.models import Sequential

original_images = os.listdir("/home/shortcut/git/untexify-data/original_images")


# The transforms compenents were chosen as follows:
# Sharpen() will preliminarily de-noise the image.
# ElasticTransform() "squiggles" the image to simulate handwriting.
# Next, we Sharpen() the image twice to severely denoise.
# Equalize() will remove color differences to match the input method on the frontend
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


def helper(index):
    # tuple-aware variable assignment
    i, j = index
    print(i)
    print()
    imagePath = "/home/shortcut/git/untexify-data/original_images/" + i
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if j % 50 == 0:
        print("This is j")
        print()
        print(j)
        print()
    # Sigma is "squiggliness", and Alpha is movement? alpha_affine is how much it moves across the page.
    # DONE: Clean up this comment.
    transformed = transform(image=image)["image"]
    transformed = np.array(transformed)
    outName = (
        "/home/shortcut/git/untexify-data/images/" + i[:-4] + "/" + str(j) + ".png"
    )

    cv2.imwrite(outName, transformed)


# Generate the class directories
for i in original_images:
    try:
        os.mkdir("/home/shortcut/git/untexify-data/images/" + i[:-4])
    except:
        pass

# Generate the dataset
with Pool(10) as p:
    p.map(
        helper, [(x, y) for x in original_images for y in range(20)]
    )  # generate the cartesian product of [ original_images ] x [ 1..20 ]
