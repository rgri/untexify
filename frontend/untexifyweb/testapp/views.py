from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import DrawingForm

import PIL
import PIL.Image
import requests
from io import BytesIO
from tensorflow import keras
from keras import layers
from keras import models
import tensorflow as tf
import numpy as np

modelDir = "/home/shortcut/git/untexify/model iterations"
HttpResponseRedirect.allowed_schemes.append("data")
# Create your views here.
def index(request):
    return render(request, "testapp/index.html", {})


def runOnTrainedModel(drawing):
    return "100"


def get_drawing(request):
    if request.method == "POST":
        form = DrawingForm(request.POST)
        if form.is_valid():
            model = keras.models.load_model(modelDir + "/webmodel/")
            image = tf.keras.utils.load_img(
                form.cleaned_data["drawingLink"], color_mode="grayscale"
            )
            image_array = tf.keras.utils.img_to_array(image)
            img_array = tf.expand_dims(image_array, 0)
            guess = np.argmax(tf.nn.softmax(model(img_array)))
            return HttpResponse(str(guess))
    form = DrawingForm()

    return render(request, "testapp/home.html", {"form": form})


def quadratic(request, x):
    output = 10
    return HttpResponse(output)
