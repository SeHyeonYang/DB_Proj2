from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *

import json

class LectureAll(View):
    def get(self, request):
        category_list = Category.objects.all()
        course_list = list()
        temp_course = Course.objects.all()
        for course in temp_course:
            temp_dict = dict()
            temp_dict['lecture_name'] = course.title
            for category in category_list:
                print(course.category_id)
                print(category.id)
                if course.category_id.id == category.id:
                    temp_dict['lecture_cate'] = category.category_name
                    break
            course_list.append(temp_dict)

        context = {}
        context['category_list'] = category_list
        context['course_list'] = course_list
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

        category_list = Category.objects.all()
        for category in category_list:
            if lecture_select == category.category_name:
                lecture = Course.objects.create(title=lecture_name, category_id=category, comments=lecture_describe)
                lecture.save()

        return HttpResponseRedirect('/app/lecture/all')

class LectureDetail(View):
    def get(self, request):
        category_list = Category.objects.all()
        searchText = request.GET.get("data")
        print(searchText)
        data = dict()
        course = Course.objects.filter(title=searchText)[0]
        course_category = Category.objects.filter(id=course.category_id.id)[0]
        data['lecture_name'] = course.title
        data['lecture_cate'] = course_category.category_name
        data['lecture_desc'] = course.comments
        data_list = list()
        data_list.append(data)
        print(data)
        context = {}
        context['category_list'] = category_list
        context['data'] = data_list
        return render(request, 'app/lecture_detail.html', context)




def lecture_check(request):
    lecture_name = request.GET.get('data')[:-1]
    print(lecture_name)
    check = Course.objects.filter(title=lecture_name).count()
    temp = dict()
    temp['distinct_check'] = check
    return HttpResponse(json.dumps(temp))


class SectionAdd(View):
    def get(self, request, lecture):
        category_list = Category.objects.all()
        data = dict()
        course = Course.objects.filter(title=lecture)[0]
        course_category = Category.objects.filter(id=course.category_id.id)[0]
        data['lecture_name'] = course.title
        data['lecture_cate'] = course_category.category_name
        data['lecture_desc'] = course.comments
        data_list = list()
        data_list.append(data)

        context = {}
        context['category_list'] = category_list
        context['data'] = data_list

        return render(request, 'app/lecture_section_add.html', context)

    def post(self, request, lecture):
        data = request.POST
        print(data)
        lecture_name = data['lecture_name']
        section_sum = data['section_sum']
        section_min_pnum = data['section_min_pnum']
        section_max_pnum = data['section_max_pnum']
        section_place = data['section_place']

        day_count = 0
        try:
            monday_button = data['monday_button']
            day_count+=1
        except:
            pass
        try:
            tuesday_button = data['tuesday_button']
            day_count+=1
        except:
            pass
        try:
            wednesday_button = data['wednesday_button']
            day_count+=1
        except:
            pass
        try:
            thursday_button = data['thursday_button']
            day_count+=1
        except:
            pass
        try:
            friday_button = data['friday_button']
            day_count+=1
        except:
            pass
        try:
            saturday_button = data['saturday_button']
            day_count+=1
        except:
            pass
        try:
            sunday_button = data['sunday_button']
            day_count+=1
        except:
            pass

        try:
            section_start_time = data['section_start_time']
        except:
            pass
        try:
            section_finish_time = data['section_finish_time']
        except:
            pass
        section_start_date = data['section_start_date']
        section_end_date = data['section_end_date']
        section_deadline = data['section_deadline']

        course = Course.objects.filter(title=lecture_name)[0]
        course_id = course.id

        section = Section.objects.create(course_id=course, start_date=section_start_date, end_date=section_end_date, times=day_count, location=section_place, price=section_sum, due_date=section_deadline, max_capacity=section_max_pnum, min_capacity=section_min_pnum, start_time=section_start_time, end_time=section_finish_time)
        section.save()

        return HttpResponseRedirect('/app/lecture/detail/?data='+course.title)




