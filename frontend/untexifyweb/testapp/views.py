from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import DrawingForm

import PIL
import os
from PIL import Image
import requests
from io import BytesIO
from tensorflow import keras
from keras import layers
from keras import models
import tensorflow as tf
import numpy as np
from urllib.request import urlopen
import pathlib
from django.conf import settings

STATIC_ROOT = settings.STATIC_ROOT
modelDir = "/home/shortcut/git/untexify/model iterations"
model = keras.models.load_model(os.path.join(STATIC_ROOT , "testapp/webmodel/"))

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
            with urlopen(form.cleaned_data["drawingLink"]) as response:
                image = Image.open(response)
                image = image.convert("L")
                image_array = tf.keras.utils.img_to_array(image)
                img_array = tf.expand_dims(image_array, 0)
                guess = np.argmax(tf.nn.softmax(model(img_array)))
            return HttpResponse(guess)
    form = DrawingForm()

    return render(request, "testapp/home.html", {"form": form})


def quadratic(request, x):
    output = 10
    return HttpResponse(output)
