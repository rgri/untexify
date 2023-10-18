import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib
import albumentations as A
import cv2
from multiprocessing import Pool

from tensorflow import keras
from keras import layers
from keras.models import Sequential

datadir = "/home/shortcut/git/untexify-data/"
original_images = os.listdir(datadir + "original_images")

# REVIEW: two passes of this- one which sets px=INT to simulate shrinking, the second to simulate shifting
# see [[id:48db14f6-5093-4fd9-b322-13736394a68a]]
rotateTransform = A.Compose(
    [
        A.CropAndPad(
            p=1,
            px=(15, 90),
            pad_cval=1000,
            pad_mode=cv2.BORDER_CONSTANT,
        ),
    ]
)
# See [[id:c77b0738-55b0-4e40-acfd-d941e8794e5d]]
wiggleTransform = A.Compose(
    [
        A.Downscale(scale_min=0.10, scale_max=0.10, p=1),
        A.ElasticTransform(alpha=20, sigma=20000, alpha_affine=10, p=1),
        A.Downscale(scale_min=0.10, scale_max=0.10, p=1),
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
    imagePath = datadir + "original_images/" + i
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if j % 50 == 0:
        print("This is j")
        print()
        print(j)
        print()
    # Sigma is "squiggliness", and Alpha is movement? alpha_affine is how much it moves across the page.
    # DONE: Clean up this comment.
    rotated = rotateTransform(image=image)["image"]
    bw_rotated = cv2.cvtColor(rotated, cv2.COLOR_RGB2GRAY)
    threshold_rotated = bw_rotated[:]
    threshold = 1

    h, b = bw_rotated.shape[:2]
    for x in range(h):
        for y in range(b):
            if bw_rotated[x][y] > threshold:
                threshold_rotated[x][y] = 255
            else:
                threshold_rotated[x][y] = 0

    wiggle_transformed = wiggleTransform(image=threshold_rotated)["image"]

    outName = datadir + "images/" + i[:-4] + "/" + str(j) + ".png"

    cv2.imwrite(outName, wiggle_transformed)


# Generate the class directories
for i in original_images:
    try:
        os.mkdir(datadir + "images/" + i[:-4])
    except:
        pass

# Generate the dataset
with Pool(15) as p:
    p.map(
        helper, [(x, y) for x in original_images for y in range(100)]
    )  # generate the cartesian product of [ original_images ] x [ 1..20 ]
