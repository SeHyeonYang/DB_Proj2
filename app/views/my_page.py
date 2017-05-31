from django.shortcuts import render


def my_page(request):
    return render(request, 'app/my_page.html', {})