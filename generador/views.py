from django.shortcuts import render
# from django.http import HttpResponse
import random

def inici(request):
    return render(request, 'inici.html')

def quant(request):
    return render(request, 'quant.html')

def contrasenya(request):
    caracters = list('abcdefghijklmnopqrstuvwxyz')
    contrasenya_generada = ''
    longitud = int(request.GET.get('length'))

    if request.GET.get('majuscules'):
        caracters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('especials'):
        caracters.extend(list('!"·$%&/()=?¿⁺*/-_:;,.'))

    if request.GET.get('nombres'):
        caracters.extend(list('01234567890'))

    for x in range(longitud):
        contrasenya_generada += random.choice(caracters)

    return render(request, 'contrasenya.html', {'contrasenya': contrasenya_generada})
