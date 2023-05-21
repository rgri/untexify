from django import forms


class DrawingForm(forms.Form):
    # It's kind of unclear in the docs what exactly
    # I have to pass to this form. According to the
    # docs, I should pass other fields of this form
    # in the first argument (in this case always
    # give it the empty dict, since there are no
    # non-image fields), and an image type in the
    # second argument.
    drawingLink = forms.CharField(widget=forms.HiddenInput)
