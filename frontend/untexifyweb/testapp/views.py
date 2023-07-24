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
model = keras.models.load_model(os.path.join(STATIC_ROOT, "testapp/webmodel/"))
class_names = [
    "cap",
    "cup",
    "geq",
    "geqslant",
    "gg",
    "ggg",
    "greaterthan",
    "in",
    "leq",
    "leqslant",
    "lessthan",
    "ll",
    "lll",
    "mathbb{A}",
    "mathbb{C}",
    "mathbb{H}",
    "mathbb{N}",
    "mathbb{O}",
    "mathbb{Q}",
    "mathbb{R}",
    "mathbb{S}",
    "mathbb{Z}",
    "ngeq",
    "ngeqslant",
    "ngtr",
    "ni",
    "nleq",
    "nleqslant",
    "nless",
    "not ubset",
    "not upset",
    "notin",
    "nprec",
    "npreceq",
    "nsubseteq",
    "nsucc",
    "nsucceq",
    "nsupseteq",
    "prec",
    "preceq",
    "setminus",
    "sqsubset",
    "sqsupset",
    "subset",
    "subset2",
    "subseteq",
    "subseteq2",
    "succ",
    "succeq",
    "supset",
    "supset2",
    "supseteq",
    "supseteq2",
]

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
                guess = class_names[np.argmax(tf.nn.softmax(model(img_array)))]
            return HttpResponse(guess)
    form = DrawingForm()

    return render(request, "testapp/home.html", {"form": form})


def quadratic(request, x):
    output = 10
    return HttpResponse(output)


def pixijs(request):
    return render(request, "testapp/thing.html")
