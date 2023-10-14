import albumentations as A
import cv2
import sys
import numpy as np

# The transforms compenents were chosen as follows:
# Sharpen() will preliminarily de-noise the image.
# ElasticTransform() "squiggles" the image to simulate handwriting.
# Next, we Sharpen() the image twice to severely denoise.
# Equalize() will remove color differences to match the input method on the frontend
# Sigma is "squiggliness", and Alpha is movement? alpha_affine is how much it moves across the page.
# p is the probability a transform will be applied
# TODO: Copy these comments to dataset.py
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

image = cv2.imread("inputimage.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated = rotateTransform(image=image)["image"]
bw_rotated = cv2.cvtColor(rotated, cv2.COLOR_RGB2GRAY)
threshold_rotated = bw_rotated[:]
threshold = 1

h, b = bw_rotated.shape[:2]
for i in range(h):
    for j in range(b):
        if bw_rotated[i][j] > threshold:
            threshold_rotated[i][j] = 255
        else:
            threshold_rotated[i][j] = 0

wiggle_transformed = wiggleTransform(image=threshold_rotated)["image"]
outName = "./outputimage.png"
cv2.imwrite(outName, wiggle_transformed)

# transformed = transform(image=image)["image"]

# transformed = np.array(transformed)
# outName = "./outputimage.png"
# cv2.imwrite(outName, transformed)
