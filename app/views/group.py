from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import json

def group_home(request):
    return render(request, 'app/group_home.html', {})