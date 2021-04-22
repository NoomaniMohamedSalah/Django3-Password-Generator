from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'generator//home.html')


def password(request):

    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('*^§?#@')

    length = int(request.GET.get('length', 12))
    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator//password.html', {'password': the_password})


def about(request):
    return render(request, 'generator//about.html')



