from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
from django.db import connection

# Create your views here.


def welcome(request):
    return render(request, 'app/course_list.html', {})


def sign_in(request):
    return render(request, 'app/sign_in.html', {})


class SignUp(View):  # 회원가입
    def get(self, request):
        return render(request, 'app/sign_up.html', {})

    def post(self, request):
        data = request.POST
        user_id = data['id']
        password = data['password']
        user_name = data['name']
        nickname = data['nickname']

        user = User.objects.create(user_id=user_id, password=password, name=user_name, nickname=nickname)
        user.save()

        return HttpResponseRedirect('/app/sign_in/')


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

