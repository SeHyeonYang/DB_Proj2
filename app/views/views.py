from django.contrib.auth import logout, login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
from .authentify import *
import json
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def teacher(request):
    teachers = Teacher.objects.all()
    teacher_info = []
    for _teacher in teachers:
        temp_dict = dict()
        temp_dict['teacher_id'] = _teacher.user_id.username
        temp_dict['phone_num'] = _teacher.phone_num
        temp_dict['email_addr'] = _teacher.email_addr
        teacher_info.append(temp_dict)
    context = {}
    context['teachers'] = teacher_info

    if request.method == "POST":
        data = request.POST
        course_name = data['search-teacher-by-course']
        courses = Course.objects.filter(title__contains=course_name).all()
        find_teacher_info = []
        for course in courses:
            for section in course.section.all():
                for teach in section.teach_set.all():
                    temp_dict = dict()
                    temp_dict['course'] = course.title
                    temp_dict['teacher_id'] = teach.teacher_id.user_id.username
                    temp_dict['phone_num'] = teach.teacher_id.phone_num
                    temp_dict['email_addr'] = teach.teacher_id.email_addr
                    find_teacher_info.append(temp_dict)
        context['find_teacher_info'] = find_teacher_info
    return render(request, 'app/teacher_tab.html', context)
