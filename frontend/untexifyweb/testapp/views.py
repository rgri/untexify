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
    "$$<$$",
    "$$>$$",
    "$$\\Delta$$",
    "$$\\Gamma$$",
    "$$\\Lambda$$",
    "$$\\Omega$$",
    "$$\\Phi$$",
    "$$\\Pi$$",
    "$$\\Psi$$",
    "$$\\Sigma$$",
    "$$\\Theta$$",
    "$$\\Upsilon$$",
    "$$\\Xi$$",
    "$$\\alpha$$",
    "$$\\amalg$$",
    "$$\\approx$$",
    "$$\\ast$$",
    "$$\\asymp$$",
    "$$\\beta$$",
    "$$\\bigcirc$$",
    "$$\\bigtriangledown$$",
    "$$\\bigtriangleup$$",
    "$$\\bowtie$$",
    "$$\\bullet$$",
    "$$\\cap$$",
    "$$\\cdot$$",
    "$$\\chi$$",
    "$$\\circ$$",
    "$$\\cong$$",
    "$$\\cup$$",
    "$$\\dagger$$",
    "$$\\dashv$$",
    "$$\\ddagger$$",
    "$$\\delta$$",
    "$$\\diamond$$",
    "$$\\digamma$$",
    "$$\\div$$",
    "$$\\doteq$$",
    "$$\\emptyset$$",
    "$$\\epsilon$$",
    "$$\\equiv$$",
    "$$\\eta$$",
    "$$\\frown$$",
    "$$\\gamma$$",
    "$$\\geq$$",
    "$$\\geqslant$$",
    "$$\\gg$$",
    "$$\\ggg$$",
    "$$\\gnapprox$$",
    "$$\\gneq$$",
    "$$\\gneqq$$",
    "$$\\gnsim$$",
    "$$\\gvertneqq$$",
    "$$\\in$$",
    "$$\\iota$$",
    "$$\\kappa$$",
    "$$\\lambda$$",
    "$$\\leq$$",
    "$$\\leqslant$$",
    "$$\\ll$$",
    "$$\\lll$$",
    "$$\\lnapprox$$",
    "$$\\lneq$$",
    "$$\\lneqq$$",
    "$$\\lnsim$$",
    "$$\\lvertneqq$$",
    "$$\\mathbb$$",
    "$$\\mathbb{A}$$",
    "$$\\mathbb{C}$$",
    "$$\\mathbb{H}$$",
    "$$\\mathbb{N}$$",
    "$$\\mathbb{O}$$",
    "$$\\mathbb{Q}$$",
    "$$\\mathbb{R}$$",
    "$$\\mathbb{S}$$",
    "$$\\mathbb{Z}$$",
    "$$\\mid$$",
    "$$\\models$$",
    "$$\\mp$$",
    "$$\\mu$$",
    "$$\\nVDash$$",
    "$$\\nVdash$$",
    "$$\\ncong$$",
    "$$\\neg$$",
    "$$\\neq$$",
    "$$\\ngeq$$",
    "$$\\ngeqq$$",
    "$$\\ngeqslant$$",
    "$$\\ngtr$$",
    "$$\\ni$$",
    "$$\\nleq$$",
    "$$\\nleqq$$",
    "$$\\nleqslant$$",
    "$$\\nless$$",
    "$$\\nmid$$",
    "$$\\not$$",
    "$$\\not\\in$$",
    "$$\\not\\subset$$",
    "$$\\not\\supset$$",
    "$$\\notin$$",
    "$$\\nparallel$$",
    "$$\\nprec$$",
    "$$\\npreceq$$",
    "$$\\nshortmid$$",
    "$$\\nshortparallel$$",
    "$$\\nsim$$",
    "$$\\nsubseteq$$",
    "$$\\nsubseteqq$$",
    "$$\\nsucc$$",
    "$$\\nsucceq$$",
    "$$\\nsupseteq$$",
    "$$\\nsupseteqq$$",
    "$$\\ntriangleleft$$",
    "$$\\ntrianglelefteq$$",
    "$$\\ntriangleright$$",
    "$$\\ntrianglerighteq$$",
    "$$\\nu$$",
    "$$\\nvDash$$",
    "$$\\nvdash$$",
    "$$\\odot$$",
    "$$\\omega$$",
    "$$\\ominus$$",
    "$$\\oplus$$",
    "$$\\oslash$$",
    "$$\\otimes$$",
    "$$\\parallel$$",
    "$$\\perp$$",
    "$$\\phi$$",
    "$$\\pi$$",
    "$$\\pm$$",
    "$$\\prec$$",
    "$$\\preceq$$",
    "$$\\precnapprox$$",
    "$$\\precneqq$$",
    "$$\\precnsim$$",
    "$$\\propto$$",
    "$$\\psi$$",
    "$$\\rho$$",
    "$$\\setminus$$",
    "$$\\sigma$$",
    "$$\\sim$$",
    "$$\\simeq$$",
    "$$\\smile$$",
    "$$\\sqcap$$",
    "$$\\sqcup$$",
    "$$\\sqsubset$$",
    "$$\\sqsubseteq$$",
    "$$\\sqsupset$$",
    "$$\\sqsupseteq$$",
    "$$\\star$$",
    "$$\\subset$$",
    "$$\\subseteq$$",
    "$$\\subsetneq$$",
    "$$\\subsetneqq$$",
    "$$\\succ$$",
    "$$\\succeq$$",
    "$$\\succnapprox$$",
    "$$\\succneqq$$",
    "$$\\succnsim$$",
    "$$\\supset$$",
    "$$\\supseteq$$",
    "$$\\supsetneq$$",
    "$$\\supsetneqq$$",
    "$$\\tau$$",
    "$$\\theta$$",
    "$$\\times$$",
    "$$\\triangleleft$$",
    "$$\\triangleright$$",
    "$$\\uplus$$",
    "$$\\upsilon$$",
    "$$\\varepsilon$$",
    "$$\\varkappa$$",
    "$$\\varnothing$$",
    "$$\\varphi$$",
    "$$\\varpi$$",
    "$$\\varrho$$",
    "$$\\varsigma$$",
    "$$\\varsubsetneq$$",
    "$$\\varsubsetneqq$$",
    "$$\\varsupsetneq$$",
    "$$\\varsupsetneqq$$",
    "$$\\vartheta$$",
    "$$\\vdash$$",
    "$$\\vee$$",
    "$$\\wedge$$",
    "$$\\wr$$",
    "$$\\xi$$",
    "$$\\zeta$$",
]

HttpResponseRedirect.allowed_schemes.append("data")


# Create your views here.
def index(request):
    return render(request, "testapp/index.html", {})


def runOnTrainedModel(drawing):
    return "100"


def get_drawing_bootstrap(request):
    if request.method == "POST":
        form = DrawingForm(request.POST)
        if form.is_valid():
            with urlopen(form.cleaned_data["drawingLink"]) as response:
                image = Image.open(response)
                image = image.convert("L")
                image_array = tf.keras.utils.img_to_array(image)
                img_array = tf.expand_dims(image_array, 0)
                updatedGuess = class_names[np.argmax(tf.nn.softmax(model(img_array)))]
            return render(
                request, "testapp/bootstrap.html", {"form": form, "guess": updatedGuess}
            )
    form = DrawingForm()
    guess = "No guess yet..."

    return render(request, "testapp/bootstrap.html", {"form": form, "guess": guess})


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


def bootstrap(request):
    return render(request, "testapp/bootstrap.html")
