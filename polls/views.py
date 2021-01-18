from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
from .models import Contact, Choise


def index(request):
    return render(request, 'index.html', {})


def photo_1(request):
    return render(request, 'photo_1.html', {})


def photo_2(request):
    return render(request, 'photo_2.html', {})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_contact = Contact(name=data['name'], phone=data['phone'], mail=data['email'], message=data['message'])
        new_contact.save()
        print(Contact.objects.all())
        return JsonResponse({'stat':'saved'})

@csrf_exempt
def choise(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_choice = Choise(name=data['name'], palet_choise=data['color_palette'], photo_choise=data['photo'])
        new_choice.save()
        return JsonResponse({'stat':'saved'})

# Create your views here.
