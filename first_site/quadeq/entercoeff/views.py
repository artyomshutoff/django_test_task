from django.shortcuts import render, redirect
import math
from .forms import ourForm

def index(request):
    submitbutton = request.POST.get("submit")

    a_coef = ''
    b_coef = ''
    c_coef = ''

    form = ourForm(request.POST)

    context = {'form': ourForm,
               'submitbutton': submitbutton,
               'a_coef': a_coef,
               'b_coef': b_coef,
               'c_coef': c_coef}

    if form.is_valid():

        request.session['a_coef'] = form.cleaned_data.get("a_coef")
        request.session['b_coef'] = form.cleaned_data.get("b_coef")
        request.session['c_coef'] = form.cleaned_data.get("c_coef")

        if request.session['a_coef'] != 0:
            return redirect('/results/')

    return render(request, 'entercoeff/index.html', context)

def results(request):

    a = request.session.get('a_coef')
    b = request.session.get('b_coef')
    c = request.session.get('c_coef')

    request.session['discr'] = b ** 2 - 4 * a * c

    request.session['x'] = 0
    request.session['x1'] = 0
    request.session['x2'] = 0

    if request.session['discr'] > 0:

        request.session['x1'] = (-b + math.sqrt(request.session['discr'])) / (2 * a)
        request.session['x2'] = (-b - math.sqrt(request.session['discr'])) / (2 * a)

    elif request.session['discr'] == 0:

        request.session['x'] = -b / (2 * a)

    return render(request, 'res_out/index.html')