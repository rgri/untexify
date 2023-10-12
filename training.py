import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib
import albumentations as A
import cv2

from tensorflow import keras
from keras import layers
from keras.models import Sequential

data_dir = pathlib.Path("/home/shortcut/git/untexify-data/images")
saved_model_path = "new_size_model/model3"

batch_size = 100
img_height = 256
img_width = 256
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    color_mode="grayscale",
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    color_mode="grayscale",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)

num_classes = 188

model = tf.keras.Sequential(
    [
        tf.keras.layers.Rescaling(
            scale=1.0 / 255, input_shape=(img_height, img_width, 1)
        ),
        tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(num_classes),
    ]
)

# Compile and display the model.
# DONE: Comment cleanup.
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

# This is a magic number.
epochs = 10
# DONE: Comment cleanup.
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label="Training Accuracy")
plt.plot(epochs_range, val_acc, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.show()
model.save(filepath="new_size_model/model3")
# Run the model on a hand-drawn example


# # For terminal usage; runs the model on the first 200 images in a pre-defined class.
#
# for i in range(200):
#     image = tf.keras.utils.load_img(
#         "/home/shortcut/git/untexify-data/images/10/" + str(i) + ".png",
#         color_mode="grayscale",
#     )
#
#     image_array = tf.keras.utils.img_to_array(image)
#     img_array = tf.expand_dims(image_array, 0)
#     class_names[np.argmax(tf.nn.softmax(model(img_array)))]
