from django.contrib.auth import logout, login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
from .authentify import *
import json


#@user_passes_test(login_required, login_url='/app/sign_in/')
def welcome(request):
    return HttpResponseRedirect('/app/lecture/all/')


def sign_in(request):
    if request.method == "GET":
        return render(request, 'app/sign_in.html', {})
    else:
        data = request.POST
        user = User.objects.filter(username=data['id'], password=data['password']).first()

        if user is None:
            return render(request, 'app/sign_in.html', {})
        else:
            login(request, user)
            return HttpResponseRedirect('/app/welcome/')


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/app/welcome/')


class SignUp(View):  # 회원가입
    # @method_decorator(user_passes_test(login_required, login_url='/app/sign_in/'))
    def get(self, request):
        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/sign_up.html', context)

    def post(self, request):
        data = request.POST
        user_id = data['user-input-id']
        password = data['password']
        last_name = data['name']
        first_name = data['nickname']

        _user = User.objects.create(username=user_id, password=password, first_name=first_name, last_name= last_name)
        #app_user = AppUser.objects.create(user=_user, name=user_name, nickname=nickname)

        if request.POST.get("chk_info") == "강사":
            phone_num = data['phone_num']
            email_addr = data['email']
            teacher = Teacher.objects.create(user_id=_user, phone_num=phone_num, email_addr=email_addr)
            category_list = Category.objects.all()
            for category in category_list:
                category_id = "category-" + str(category.id)
                if category_id in data:
                    cate = TeacherCategory.objects.create(teacher_id=teacher, category_id=category)
                    cate.save()
            teacher.save()
        _user.save()
        #app_user.save()
        return HttpResponseRedirect('/app/sign_in/')


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def id_check(request):
    user_id = request.GET.get('data')[:-1]
    check = User.objects.filter(username=user_id).count()
    temp = dict()
    temp['distinct_check'] = check
    return HttpResponse(json.dumps(temp))


def leave(request):
    user = User.objects.filter(username=request.user)
    logout(request)
    user.delete()
    return HttpResponseRedirect('/app/welcome/')
