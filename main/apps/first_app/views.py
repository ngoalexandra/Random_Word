from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
unique_id = get_random_string(length = 14)

def index(request):
    return render(request, 'first_app/index.html')

def generate(request):
    request.session['random_word'] = unique_id
    if 'number' not in request.session:
        request.session['number'] = 1
    else: 
        request.session['number'] +=1
    return redirect('/')
def reset(request):
    request.session['number'] = 0
    return redirect('/')

# def generate(request):
