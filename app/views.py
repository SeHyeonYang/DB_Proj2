from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'app/class_list.html', {})
