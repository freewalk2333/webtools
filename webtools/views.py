from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tools.generator import generate_idcard_frontside, generate_idcard_backside
import json

@csrf_exempt
def webtools(request):
    if request.method == 'GET':
        return render(request=request, template_name='webtools.html')
    else:
        data = {
            'name': request.POST['name'],
            'idno': request.POST['idno'],
            'address': request.POST['address']
        }
        print(data)
        return JsonResponse(data)


@csrf_exempt
def portrait(request):
    if request.method == 'GET':
        return render(request=request, template_name='portrait.html')
    else:
        name = request.POST['name']
        idno = request.POST['idno']
        address = request.POST['address']
        idno_base64 = generate_idcard_frontside(name=name, idno=idno, address=address)
        body = {
            'idno_base64': idno_base64,
        }

        return JsonResponse(body)


@csrf_exempt
def emblem(request):
    if request.method == 'GET':
        return render(request=request, template_name='emblem.html')
    else:
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        idno_base64= generate_idcard_backside(date_start=date_start, date_end=date_end)
        body = {
            'idno_base64': idno_base64,
        }
        return JsonResponse(body)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request=request, template_name='index.html')
    else:
        name = request.POST['name']
        idno = request.POST['idno']
        address = request.POST['address']
        idno_base64 = generate_idcard_frontside(name=name, idno=idno, address=address)
        body = {
            'idno_base64': idno_base64,
        }

        return JsonResponse(body)