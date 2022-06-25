from django import forms

class ourForm(forms.Form):

    a_coef = forms.FloatField(label="a")
    b_coef = forms.FloatField(label="b")
    c_coef = forms.FloatField(label="c")