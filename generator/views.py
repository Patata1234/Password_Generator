from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'layouts/home.html')

def about(request):
    return render (request, 'layouts/about.html')

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET['length'])

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRS'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-+=¿¡/[]´¨¨"";:,.<>\|'))


    for x in range(length):
        generated_password += random.choice(characters)

    return render (request, 'layouts/password.html',{
        'password': generated_password
    })