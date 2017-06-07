from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *

import json


def lecture_all(request):
    category_list = Category.objects.all()
    for category in category_list:
        temp_dict = dict()
        temp_dict['category_id'] = category.id
        temp_dict['category_name'] = category.category_name
    context = {}
    context['category_list'] = category_list
    return render(request, 'app/lecture_all.html', context)

class LectureAll(View):
    def get(self, request):
        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/lecture_all.html', context)

    def post(self, request):

        return HttpResponseRedirect('/app/lecture/add/')

def lecture_category(request):
    return render(request, '', {})


class LectureAdd(View):  # 강좌 개설
    def get(self, request):
        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/lecture_add.html', context)

    @csrf_exempt
    def post(self, request):
        data = request.POST
        lecture_select = data['lecture_select']
        lecture_name = data['lecture-name']
        lecture_describe = data['lecture_describe']
        print(data)

        category_list = Category.objects.all()
        for category in category_list:
            if lecture_select == category.category_name:
                print("카테고리 이름 : " + category.category_name)
                lecture = Course.objects.create(title=lecture_name, category_id=category, comments=lecture_describe)
                lecture.save()

        return HttpResponseRedirect('/app/lecture/all')


class SectionAdd(View):
    def get(self, request):
        category_list = Category.objects.all()

        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return HttpResponseRedirect('/app/lecture/all')

    def post(self, request):
        data = request.POST
        lecture_sum = data['lecture_sum']
        lecture_min_pnum = data['lecture_min_pnum']
        lecture_max_pnum = data['lecture_max_pnum']
        lecture_place = data['lecture_place']
        monday_button = data['monday_button']
        tuesday_button = data['tuesday_button']
        wednesday_button = data['wednesday_button']
        thursday_button = data['thursday_button']
        friday_button = data['friday_button']
        saturday_button = data['saturday_button']
        sunday_button = data['sunday_button']
        lecture_start_time = data['lecture_start_time']
        lecture_finish_time = data['lecture_finish_time']


def lecture_check(request):
    lecture_name = request.GET.get('data')[:-1]
    print(lecture_name)
    check = Course.objects.filter(title=lecture_name).count()
    temp = dict()
    temp['distinct_check'] = check
    return HttpResponse(json.dumps(temp))