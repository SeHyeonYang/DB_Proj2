from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'app/class_list.html', {})


def sign_in(request):
    return render(request, 'app/sign_in.html', {})


def sign_up(request):
    return render(request, 'app/sign_up.html', {})

