from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def welcome(request):
    return render(request, 'app/course_list.html', {})


def sign_in(request):
    return render(request, 'app/sign_in.html', {})

class SignUp(View):  # 회원가입
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
        user_name = data['name']
        nickname = data['nickname']

        user = User.objects.create(user_id=user_id, password=password, name=user_name, nickname=nickname)

        if request.POST.get("chk_info") == "강사":
            phone_num = data['phone_num']
            email_addr = data['email']
            teacher = Teacher.objects.create(user_id=user, phone_num=phone_num, email_addr=email_addr)
            category_list = Category.objects.all()
            for category in category_list:
                category_id = "category-" + str(category.id)
                if category_id in data:
                    cate = TeacherCategory.objects.create(teacher_id=teacher, category_id=category)
                    cate.save()
            teacher.save()
        user.save()
        return HttpResponseRedirect('/app/sign_in/')


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def id_check(request):
    user_id = request.GET.get('data')[:-1]
    check = User.objects.filter(user_id=user_id).count()
    temp = dict()
    temp['distinct_check'] = check
    return HttpResponse(json.dumps(temp))
