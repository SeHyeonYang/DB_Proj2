from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
from django.db.models import F

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
                if course.category_id.id == category.id:
                    temp_dict['lecture_cate'] = category.category_name
                    break
            course_list.append(temp_dict)

        flag = Teacher.objects.filter(user_id=request.user).count()
        context = {}
        context['category_list'] = category_list
        context['course_list'] = course_list
        context['is_teacher'] = flag
        return render(request, 'app/lecture_all.html', context)

    def post(self, request):
        data = request.POST
        if (data['option'] == 'search') :
            category_list = Category.objects.all()
            course_list = list()
            temp_course_list = Course.objects.filter(title__contains=data['search']).all()
            for course in temp_course_list:
                temp_dict = dict()
                temp_dict['lecture_name'] = course.title
                for category in category_list:
                    if course.category_id.id == category.id:
                        temp_dict['lecture_cate'] = category.category_name
                        break
                course_list.append(temp_dict)

            flag = Teacher.objects.filter(user_id=request.user).count()
            context = {}
            context['category_list'] = category_list
            context['course_list'] = course_list
            context['is_teacher'] = flag
            return render(request, 'app/lecture_all.html', context)
        elif (data['option'] == 'lecture_add') :
            return HttpResponseRedirect('/app/lecture/add/')
        else :
            return HttpResponse("ERROR : 잘못된 입력입니다.")


def lecture_category(request, category):
    category_list = Category.objects.all()
    category_qs = Category.objects.filter(category_name=category)[0]
    print(category_qs.category_name)
    course_list = list()

    if request.method == "POST":
        data = request.POST
        if (data['option'] == 'search'):
            courses = Course.objects.filter(category_id=category_qs, title__contains=data['search']).all()
        elif (data['option'] == 'lecture_add'):
            context = {}
            context['category'] = category
            return HttpResponseRedirect('/app/lecture/add/?data=' + category)
        else:
            HttpResponse("잘못된 입력입니다.")
    else :
        courses = Course.objects.filter(category_id=category_qs).all()

    print(courses.count())
    for course in courses:
        temp_dict = dict()
        temp_dict['title'] = course.title
        temp_dict['category_name'] = category
        print(temp_dict)
        course_list.append(temp_dict)

    context = {}
    context['category'] = category
    context['category_list'] = category_list
    context['course_list'] = course_list
    return render(request, 'app/lecture_category.html', context)


class LectureAdd(View):  # 강좌 개설
    def get(self, request):
        data = request.GET
        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        if data :
            context['category'] = data['data']
        else :
            context['category'] = "all"
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

        section_list = list()

        temp_section_list = Section.objects.filter(course_id=course).all().order_by('due_date')
        for temp in temp_section_list:
            user_count = Take.objects.filter(section_id=temp).count()
            temp_dict = dict()
            temp_dict['section_id'] = temp.id
            temp_dict['start_date'] = temp.start_date
            temp_dict['end_date'] = temp.end_date
            temp_dict['times'] = temp.times
            temp_dict['location'] = temp.location
            temp_dict['price'] = temp.price
            temp_dict['due_date'] = temp.due_date
            temp_dict['max_capacity'] = temp.max_capacity
            temp_dict['min_capacity'] = temp.min_capacity
            temp_dict['cur_pnum'] = user_count
            temp_dict['start_time'] = temp.start_time
            temp_dict['end_time'] = temp.end_time
            try:
                teacher = Teach.objects.filter(section_id=temp)[0]
                user = User.objects.filter(user_id=teacher).first()
                temp_dict['teacher'] = user.username
            except:
                temp_dict['teacher'] = ""
                pass
            section_list.append(temp_dict)

        flag = Teacher.objects.filter(user_id=request.user).count()
        context = {}
        context['category_list'] = category_list
        context['data'] = data_list
        context['section_list'] = section_list
        context['is_teacher'] = flag
        return render(request, 'app/lecture_detail.html', context)

    def post(self, request):
        data = request.POST
        print(data)

        section_data = data['section_enroll']
        lecture_name = data['lecture_name']

        section = Section.objects.filter(id=int(section_data)).first()
        take = Take.objects.create(user_id=request.user, section_id=section)
        take.save()

        return HttpResponseRedirect('/app/lecture/detail/?data=' + lecture_name)


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

        teacher = Teacher.objects.filter(user_id=request.user).first()
        teach = Teach.objects.create(teacher_id=teacher, section_id=section)
        teach.save()

        return HttpResponseRedirect('/app/lecture/detail/?data=' + course.title)




