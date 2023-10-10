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
transform = A.Compose(
    [
        A.Downscale(scale_min=0.07, scale_max=0.07, p=1),
        # A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        A.ElasticTransform(alpha=20, sigma=20000, alpha_affine=10, p=1),
        A.Downscale(scale_min=0.07, scale_max=0.07, p=1),
        # A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        # A.Sharpen(alpha=(1, 1), lightness=(1.0, 1.0), p=1.0),
        A.Equalize(p=1.0),
    ]
)

# Get the first command line argument- sys.argv[0] is always the command itself
image = cv2.imread("inputimage.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

transformed = transform(image=image)["image"]
transformed = np.array(transformed)
outName = "./outputimage.png"

cv2.imwrite(outName, transformed)
