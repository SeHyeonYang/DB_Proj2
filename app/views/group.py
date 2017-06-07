from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import json


def group_home(request):
    return render(request, 'app/group_home.html', {})


def group_create(request):
    category_list = Category.objects.all()

    for category in category_list:
        temp_dict = dict()
        temp_dict['category_id'] = category.id
        temp_dict['category_name'] = category.category_name
    context = []
    context['category_list'] = category_list
    return render(request, 'app/group_create.html', context)


def group_private(request):
    return render(request, 'app/group_private.html',{})
