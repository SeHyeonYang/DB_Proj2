from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import json


def group_home(request):
    return render(request, 'app/group_home.html', {})


def group_create(request):
    if request.method == "GET":
        return render(request, 'app/group_create.html', {})
    else:
        data = request.POST
        group_name = data['group_name']
        print(str(group_name))
        return render(request, 'app/group_create.html', {})

def group_private(request):
    return render(request, 'app/group_private.html',{})