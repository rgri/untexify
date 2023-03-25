import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib

# .Path()'s need an absolute path
data_dir = pathlib.Path("/home/shortcut/envs/tf_wsl/tf_project/images/")
image_count = len(list(data_dir.glob("*.png")))
print(image_count)
batch_size = 10
img_height = 72
img_width = 72
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
class_names = train_ds.class_names

# Display first nine images in the data_set.
# plt.figure(figsize=(10, 10))
# for images, labels in data_set.take(1):
#     for i in range(9):
#         ax = plt.subplot(3, 3, i + 1)
#         plt.imshow(images[i].numpy().astype("uint8"))
#         plt.title(class_names[labels[i]])
#         plt.axis("off")
# plt.show()
num_classes = len(class_names)
