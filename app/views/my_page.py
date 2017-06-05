from django.shortcuts import render
from .authentify import *


def my_page(request, menu):
    user = request.user
    context = dict()
    context['my_info'] = user
    context['is_teacher'] = is_teacher(user)
    if menu == "info":
        return render(request, 'app/my_page_info.html', context)
    elif menu == "friend":
        return render(request, 'app/my_page_friend.html', {})
    elif menu == "lecture":
        return render(request, 'app/my_page_lecture.html', {})
    return render(request, 'app/my_page_info.html', {})
