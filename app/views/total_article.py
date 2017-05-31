from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import json

def total_article(request):
    return render(request, 'app/total_article.html', {})