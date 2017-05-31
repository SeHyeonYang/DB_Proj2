from django.shortcuts import render


def lecture_add(request):
    return render(request, 'app/lecture_add.html', {})